import streamlit as st
from openai import OpenAI

# --- App Configuration ---
st.set_page_config(
    page_title="AI Script Generator",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- App Title and Description ---
st.title("AI Script Generator (Fine-tuned ChatGPT)")
st.markdown("""
Welcome to the AI Script Generator! This app uses a fine-tuned ChatGPT model to generate a creative Reel/Ad script for your app or product.

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
        try:
            with st.spinner("Generating your script..."):
                # Initialize the OpenAI client with the API key from secrets
                client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                
                # Create the prompt for the fine-tuned model
                prompt = f"""
                Generate a creative script based on the following details:
                
                App Description: {app_description}
                Target Audience: {target_audience}
                Goal: {goal}
                
                Please provide a creative and engaging script that meets these requirements.
                """
                
                # Make the API call to the fine-tuned model
                response = client.chat.completions.create(
                    model="ft:gpt-4.1-nano-2025-04-14:personal:3-content-script-generator:Bvj2a1H5",
                    messages=[
                        {"role": "system", "content": "You are a creative script writer who specializes in creating engaging and effective ad scripts."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )
                
                # Extract and display the generated script
                script = response.choices[0].message.content
                
                # Clean up the script formatting
                if script:
                    # Replace escaped newlines with actual newlines
                    script = script.replace('\\n', '\n')
                    # Remove any quotes at the beginning and end if present
                    script = script.strip('"')
                    
                    st.markdown("### 🎬 Your Generated Reel/Ad Script")
                    st.markdown("---")
                    
                    # Display the script in a nice formatted way
                    st.text_area(
                        "Generated Script:",
                        value=script,
                        height=400,
                        disabled=True
                    )
                    
                    # Also show it as markdown for better readability
                    with st.expander("📝 Formatted View"):
                        st.markdown(script)
                else:
                    st.error("No script was generated. Please try again.")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
