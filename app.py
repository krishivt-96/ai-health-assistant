import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# --- Configuration ---
st.set_page_config(
    page_title="AI Food & Health Assistant",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="expanded",
)


# --- Initialize Gemini ---
@st.cache_resource
def configure_gemini():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return False
    genai.configure(api_key=api_key)
    return True

is_configured = configure_gemini()

# Use Gemini 1.5 Flash for fast, lightweight responses
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Helper Function for Generation ---
def generate_response(prompt):
    if not is_configured:
        return "⚠️ Please set your `GEMINI_API_KEY` environment variable to generate responses."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating response: {e}"

# --- UI Layout ---
st.title("🥗 AI Food & Health Assistant")
st.markdown("**Your smart companion for better food choices and personalized health advice.**")

if not is_configured:
    st.error("⚠️ GEMINI_API_KEY environment variable not found. The AI features will not work until this is set.")

tab1, tab2, tab3 = st.tabs(["📅 Meal Planner", "🔍 Food Analyzer", "💡 Smart Daily Suggestion"])

# --- Tab 1: Meal Planner ---
with tab1:
    st.header("Personalized Meal Planner")
    st.markdown("Generate a custom meal plan based on your goals, diet, and budget.")
    
    with st.form("meal_planner_form"):
        col1, col2 = st.columns(2)
        with col1:
            goal = st.text_input("Goal (e.g., Weight loss, Muscle gain, Maintenance)", placeholder="Weight loss")
            diet = st.selectbox("Dietary Preference", ["None", "Vegetarian", "Vegan", "Keto", "Paleo", "Mediterranean"])
        with col2:
            budget = st.selectbox("Budget", ["Low", "Medium", "High"])
            allergies = st.text_input("Allergies / Restrictions", placeholder="e.g., Peanuts, Dairy, Gluten")
            
        submit_planner = st.form_submit_button("Generate Plan ✨")
        
    if submit_planner:
        if not goal:
            st.warning("Please enter a goal.")
        else:
            with st.spinner("Generating your personalized meal plan..."):
                prompt = f"""
                You are an expert nutritionist. Create a detailed 1-day meal plan based on the following constraints:
                - Goal: {goal}
                - Diet: {diet}
                - Budget: {budget}
                - Allergies/Restrictions: {allergies if allergies else 'None'}
                
                Please format your response beautifully using markdown and structure it exactly as follows:
                
                ## 🍽️ Meals
                (List breakfast, lunch, dinner, and snacks with appetizing names and brief descriptions)
                
                ## 📊 Estimated Calories & Macros
                (Total calories and macro breakdown for the whole day)
                
                ## 📖 Quick Recipes
                (Short, easy-to-follow recipes for the main meals)
                
                ## 💡 Health Tips
                (2-3 actionable tips tailored to the user's specific goal and diet)
                """
                result = generate_response(prompt)
                st.markdown(f"<div style='padding: 20px; background-color: white; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>{result}</div>", unsafe_allow_html=True)

# --- Tab 2: Food Analyzer ---
with tab2:
    st.header("Smart Food Analyzer")
    st.markdown("Analyze a specific food item or meal for its nutritional profile and get healthier alternatives.")
    
    with st.form("food_analyzer_form"):
        food_item = st.text_input("Food Item", placeholder="e.g., Double Cheeseburger, Quinoa Salad, Pad Thai")
        submit_analyzer = st.form_submit_button("Analyze Food 🔍")
        
    if submit_analyzer:
        if not food_item:
            st.warning("Please enter a food item.")
        else:
            with st.spinner("Analyzing nutritional profile..."):
                prompt = f"""
                You are a nutrition expert. Analyze the following food item or meal: "{food_item}"
                
                Please format your response beautifully using markdown and structure it exactly as follows:
                
                ## 📊 Estimated Calories & Macros
                (Provide reasonable estimates for a standard portion size. State the portion size clearly.)
                
                ## 🩺 Health Rating
                (Rate it from 1-10 on a health scale. Explain why it received this score in 1-2 sentences.)
                
                ## 🥗 Better Alternatives
                (Suggest 2-3 healthier, satisfying alternatives that fulfill a similar craving, and briefly explain why they are better.)
                """
                result = generate_response(prompt)
                st.markdown(f"<div style='padding: 20px; background-color: white; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>{result}</div>", unsafe_allow_html=True)

# --- Tab 3: Smart Daily Suggestion ---
with tab3:
    st.header("Smart Daily Suggestion")
    st.markdown("Tell me what you've eaten so far today, and I'll help you balance the rest of your day.")
    
    with st.form("daily_suggestion_form"):
        ate_today = st.text_area("What did you eat today?", placeholder="e.g., 2 slices of pepperoni pizza for lunch, an apple, and a latte.", height=120)
        submit_suggestion = st.form_submit_button("Get Suggestions 💡")
        
    if submit_suggestion:
        if not ate_today:
            st.warning("Please enter what you ate today.")
        else:
            with st.spinner("Evaluating your daily intake..."):
                prompt = f"""
                You are a health and nutrition coach. The user has eaten the following so far today: "{ate_today}"
                
                Based on this input, provide actionable advice formatted beautifully in markdown, structured exactly as follows:
                
                ## 📈 Health Impact
                (Briefly and kindly analyze the nutritional impact of what they've eaten so far. E.g., "You've had a lot of carbs and sodium but are low on protein and greens.")
                
                ## 🍽️ What to Eat Next
                (Suggest 2 specific, appetizing meals or snacks to eat next to balance their macros and micronutrients for the day.)
                
                ## ⚖️ How to Balance Diet
                (Provide 2 practical tips on how to balance their diet for the rest of the day or tomorrow to compensate for today's intake.)
                """
                result = generate_response(prompt)
                st.markdown(f"<div style='padding: 20px; background-color: white; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>{result}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>Powered by Google Gemini 1.5 Flash & Streamlit</p>", unsafe_allow_html=True)
