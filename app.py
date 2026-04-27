import streamlit as st

st.set_page_config(page_title="AI Food & Health Assistant")

st.title("AI Food & Health Assistant")

st.subheader("Personalized Meal Planner")

goal = st.text_input("Goal")
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
diet = st.selectbox("Diet", ["None", "Keto", "Vegan"])
allergy = st.text_input("Allergies")

if st.button("Generate Plan"):
    st.success("Working 🎉")

    st.write("Sample Meal Plan:")
    st.write("- Rice + Dal")
    st.write("- Eggs / Paneer")
    st.write("- Fruits")