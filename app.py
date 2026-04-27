import streamlit as st

st.set_page_config(page_title="AI Food & Health Assistant")

st.title("AI Food & Health Assistant")

st.subheader("Personalized Meal Planner")

goal = st.text_input("Goal (e.g., Weight loss, Muscle gain)")
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
diet = st.selectbox("Dietary Preference", ["None", "Keto", "Vegan"])
allergy = st.text_input("Allergies / Restrictions")

if st.button("Generate Plan"):
    st.success("Here’s your plan:")
    
    st.markdown("""
    ### 🥗 Health Impact
    Balanced and aligned with your goal.

    ### 🍽 What to Eat
    - Grilled chicken / paneer  
    - Rice + veggies  
    - Fruits  

    ### ⚖️ Tips
    - Maintain protein intake  
    - Avoid junk food  
    """)