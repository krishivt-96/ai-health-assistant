# AI Food & Health Assistant 🥗

A lightweight, visually appealing Streamlit-based web application powered by Google's Gemini API. It is designed to help users make better food choices using context and behavior.

## Features ✨

1. **📅 Meal Planner**
   - Inputs: Goal, diet preference, budget, allergies.
   - Output: Generates personalized meals, calorie estimates, quick recipes, and health tips.

2. **🔍 Food Analyzer**
   - Input: Any food item or meal.
   - Output: Provides estimated calories/macros, a health rating (1-10), and healthier alternatives.

3. **💡 Smart Daily Suggestion**
   - Input: What you have eaten so far today.
   - Output: Evaluates health impact, suggests what to eat next to balance macros, and provides diet-balancing tips.

---

## 🚀 Local Setup & Running

1. **Clone or navigate to the directory**:
   ```bash
   cd ai-health-assistant
   ```

2. **Install dependencies**:
   *(Optional: Create a virtual environment first)*
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API Key**:
   You need a Google Gemini API key to use the features.
   ```bash
   # On macOS/Linux
   export GEMINI_API_KEY="your_actual_api_key_here"
   
   # On Windows (Command Prompt)
   set GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   The app will automatically open in your browser at `http://localhost:8501`.

---

## ☁️ Deployment to GCP Cloud Run

This project is fully containerized and optimized to be lightweight (<1MB source) for deploying to **Google Cloud Run**.

1. **Prerequisites**:
   - Install the Google Cloud SDK (`gcloud` CLI).
   - Ensure you are authenticated (`gcloud auth login`) and have a project selected.
   - Ensure the **Cloud Run** and **Cloud Build** APIs are enabled for your project.

2. **Deploy the container**:
   Run the following command in the same directory as the `Dockerfile`.
   Replace `AIzaSyDz6jZCZGn4qDjT3BbRsp5b6hDd8RWo1sI` with your real Gemini API key.

   ```bash
   gcloud run deploy ai-health-assistant \
     --source . \
     --port 8080 \
     --allow-unauthenticated \
     --set-env-vars="GEMINI_API_KEY=your_actual_api_key_here"
   ```

3. **Success!** 
   `gcloud` will provide you with a public URL where your app is hosted securely.

---
*Powered by [Streamlit](https://streamlit.io/) and [Google Gemini](https://deepmind.google/technologies/gemini/)*
