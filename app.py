import streamlit as st
import google.generativeai as genai
import time

# --- App Configuration ---
st.set_page_config(
    page_title="AI Script Generator",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- Get API Key from Streamlit secrets ---
gemini_api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=gemini_api_key)

# --- App Title and Description ---
st.title("🎬 AI Script Generator")
st.markdown("""
Welcome to the AI Script Generator! This app uses Google's Gemini model to generate a creative Reel/Ad script for your app or product.

**How it works:**
1. Fill out the form below with your app details.
2. Click 'Generate Script'.
3. Get a ready-to-use script for your next Reel or Ad!
""")

# --- Script Generation Form ---
with st.form("script_form"):
    app_description = st.text_area("Describe your app", help="What does your app do? What makes it unique?")
    target_audience = st.text_input("Who is your target audience?", help="e.g., College students, young adults, etc.")
    goal = st.text_input("What is your goal?", value="Generate a Reel script for my app.")
    submitted = st.form_submit_button("Generate Script")

if submitted:
    if not app_description or not target_audience or not goal:
        st.warning("Please fill in all fields to generate a script.")
    else:
        # Prepare the prompt in the fine-tuned format
        user_input = {
            "app_description": app_description,
            "target_audience": target_audience,
            "goal": goal
        }
        prompt = str(user_input)

        # Gemini model setup
        system_instruction = (
            "You are a creative AI scriptwriting assistant. "
            "Given the user's app description, target audience, and goal, generate a creative, engaging, and detailed script for a social media Reel or Ad. "
            "Format your response with clear segment timings, visual and audio cues, and a strong call to action, similar to the provided examples."
        )
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=system_instruction
        )
        try:
            with st.spinner("Generating your script..."):
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("Your Generated Reel/Ad Script")
                st.markdown(response.text if hasattr(response, 'text') else str(response))
        except Exception as e:
            st.error(f"An error occurred: {e}")
