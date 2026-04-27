# Use lightweight Python 3.11 image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies without caching to keep image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Expose port for GCP Cloud Run
EXPOSE 8080

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
