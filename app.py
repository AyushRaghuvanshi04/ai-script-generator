import streamlit as st
import requests

# --- App Configuration ---
st.set_page_config(
    page_title="AI Script Generator",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- App Title and Description ---
st.title("AI Script Generator (Gemini via HTTP)")
st.markdown("""
Welcome to the AI Script Generator! This app uses Google's Gemini model to generate a creative Reel/Ad script for your app or product.

**How it works:**
1. Fill out the form below with your app details.
2. Click 'Generate Script'.
3. Get a ready-to-use script for your next Reel or Ad!
""")

# --- Script Generation Form ---
with st.form("script_form"):
    app_description = st.text_area("Describe your app")
    target_audience = st.text_input("Who is your target audience?")
    goal = st.text_input("What is your goal?", value="Generate a Reel script for my app.")
    submitted = st.form_submit_button("Generate Script")

if submitted:
    if not app_description or not target_audience or not goal:
        st.warning("Please fill in all fields to generate a script.")
    else:
        api_key = st.secrets["GEMINI_API_KEY"]
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        prompt = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": f"app_description: {app_description}\ntarget_audience: {target_audience}\ngoal: {goal}"
                        }
                    ]
                }
            ]
        }
        try:
            with st.spinner("Generating your script..."):
                response = requests.post(endpoint, headers=headers, json=prompt)
                response.raise_for_status()
                result = response.json()
                # Gemini returns candidates, get the first one
                script = result["candidates"][0]["content"]["parts"][0]["text"]
                st.markdown("### Your Generated Reel/Ad Script")
                st.markdown(script)
        except Exception as e:
            st.error(f"An error occurred: {e}")
