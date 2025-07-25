import streamlit as st
from openai import OpenAI
import time
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.let_it_rain import rain
from streamlit_lottie import st_lottie
import json
import requests

def load_lottie_file(filepath: str):
    import json
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading Lottie file: {e}")
        return None

# Custom CSS for modern UI
st.set_page_config(
    page_title="✨ AI Script Generator",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: #0f172a !important;
        color: #e2e8f0 !important;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header Styles */
    .main-title {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        background: linear-gradient(45deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important;
    }
    
    /* Card Styles */
    .card {
        background: rgba(30, 41, 59, 0.8) !important;
        border-radius: 12px !important;
        padding: 1.5rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3) !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 1.5rem;
        color: #e2e8f0 !important;
    }
    
    /* Button Styles */
    .stButton>button {
        background: linear-gradient(45deg, #6366f1, #7c3aed) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        text-transform: none;
        letter-spacing: 0.5px;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3) !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(99, 102, 241, 0.3) !important;
    }
    
    /* Input Fields */
    .stTextArea>div>div>textarea, 
    .stTextInput>div>div>input {
        border-radius: 10px !important;
        background-color: rgba(15, 23, 42, 0.8) !important;
        border: 2px solid #334155 !important;
        color: #e2e8f0 !important;
        padding: 0.8rem 1rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea>div>div>textarea:focus, 
    .stTextInput>div>div>input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
        background-color: rgba(15, 23, 42, 1) !important;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1e293b;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #4f46e5;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #6366f1;
    }
    
    /* Animation Classes */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out forwards;
    }
    
    /* Tags */
    .tag {
        display: inline-block;
        background: rgba(79, 70, 229, 0.2);
        color: #a5b4fc;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
        margin: 0.25rem;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    /* Timeline Styles */
    .timeline-item {
        background: rgba(30, 41, 59, 0.6);
        border-left: 4px solid #6366f1;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    
    .timeline-time {
        color: #a5b4fc;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .timeline-content {
        color: #e2e8f0;
        line-height: 1.6;
    }
    
    /* Visual Timeline Styles */
    .visual-timeline {
        background: rgba(30, 41, 59, 0.8);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .timeline-header {
        color: #e2e8f0;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .timeline-container {
        display: flex;
        align-items: center;
        gap: 0;
        margin: 1rem 0;
        overflow-x: auto;
        padding: 0.5rem 0;
    }
    
    .timeline-segment {
        flex: 1;
        min-width: 120px;
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        height: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 0.8rem;
        font-weight: 500;
        border-radius: 8px;
        margin: 0 2px;
        position: relative;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .timeline-segment:hover {
        transform: translateY(-2px);
        border-color: #a5b4fc;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }
    
    .timeline-segment.hook {
        background: linear-gradient(135deg, #ef4444, #f97316);
    }
    
    .timeline-segment.problem {
        background: linear-gradient(135deg, #f59e0b, #eab308);
    }
    
    .timeline-segment.solution {
        background: linear-gradient(135deg, #10b981, #059669);
    }
    
    .timeline-segment.demo {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
    }
    
    .timeline-segment.cta {
        background: linear-gradient(135deg, #8b5cf6, #7c3aed);
    }
    
    .segment-time {
        font-size: 0.7rem;
        font-weight: 600;
        margin-bottom: 2px;
    }
    
    .segment-title {
        font-size: 0.75rem;
        text-align: center;
        line-height: 1.2;
    }
    
    .timeline-progress {
        width: 100%;
        height: 4px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 2px;
        margin: 1rem 0 0.5rem 0;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        border-radius: 2px;
        width: 0%;
        animation: progressFill 2s ease-out forwards;
    }
    
    @keyframes progressFill {
        from { width: 0%; }
        to { width: 100%; }
    }
</style>
""", unsafe_allow_html=True)

# --- App Header ---
col1, col2 = st.columns([1, 3])
with col1:
    # Try to load local Lottie file, fallback to emoji
    lottie_animation = load_lottie_file("assets/animation.json")
    if lottie_animation:
        st_lottie(
            lottie_animation,
            height=120,
            width=120,
            key="lottie"
        )
    else:
        st.markdown("<div style='font-size: 100px; text-align: center;'>🎬</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<h1 class='main-title'>AI Script Generator</h1>", unsafe_allow_html=True)
    st.caption("Powered by Fine-tuned GPT-4.1 Nano")

# --- How it Works ---
with st.container():
    st.markdown("""
    <div class='card fade-in' style='margin-bottom: 1.5rem;'>
        <h3>🎯 How It Works</h3>
        <ol style='padding-left: 1.5rem; margin: 0.5rem 0;'>
            <li>Fill out the form below with your app details</li>
            <li>Click 'Generate Script'</li>
            <li>Get a viral-worthy script in seconds! 🚀</li>
        </ol>
        <div style='margin-top: 0.5rem;'>
            <span class='tag'>#AIGenerated</span>
            <span class='tag'>#ViralContent</span>
            <span class='tag'>#ContentCreator</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Script Generation Form ---
with st.container():
    with st.form("script_form"):
        st.markdown("<div class='card fade-in' style='padding: 1.5rem;'>", unsafe_allow_html=True)
        
        st.markdown("### 🎨 App Details")
        
        # Basic Information
        st.markdown("#### 📱 Basic Information")
        app_name = st.text_input(
            "App Name",
            placeholder="e.g., Duolingo, Instagram, Spotify"
        )
        
        app_description = st.text_area(
            "App Description",
            placeholder="Brief description of your app or product"
        )
        
        target_audience = st.text_area(
            "Target Audience",
            placeholder="Detailed description of your target audience (age, interests, behaviors)"
        )
        
        # Key Features
        st.markdown("#### ⭐ Key Features to Highlight")
        features = []
        for i in range(3):  # Allow up to 3 key features
            feature = st.text_input(
                f"Feature {i+1}",
                placeholder=f"Enter feature {i+1} (leave blank if not needed)",
                key=f"feature_{i}"
            )
            if feature:  # Only add non-empty features
                features.append(feature)
        
        # Script Details
        st.markdown("#### 🎭 Script Details")
        tone_of_voice = st.selectbox(
            "Tone of Voice",
            ["Humorous", "Professional", "Friendly", "Inspirational", "Casual", "Authoritative"],
            index=0
        )
        
        desired_format_trend = st.selectbox(
            "Desired Format/Trend",
            ["POV Style", "Testimonial", "Before/After", "Tutorial", "Behind the Scenes", "Challenge"],
            index=0
        )
        
        contextual_angle = st.text_area(
            "Contextual Angle",
            placeholder="Any specific context or scenario for the script (e.g., 'It's Friday afternoon at 4 PM...')"
        )
        
        negative_constraint = st.text_area(
            "Negative Constraints",
            placeholder="Anything specific to avoid in the script (e.g., 'Do not mention that the app is free')",
            help="Leave blank if there are no specific constraints"
        )
        
        # Animated submit button
        submitted = st.form_submit_button(
            "🚀 Generate Script",
            use_container_width=True
        )
        
        st.markdown("</div>", unsafe_allow_html=True)

if submitted:
    # Validate required fields
    required_fields = {
        "App Name": app_name,
        "App Description": app_description,
        "Target Audience": target_audience
    }
    missing_fields = [field for field, value in required_fields.items() if not value.strip()]
    
    if missing_fields:
        st.warning(f"Please fill in all required fields: {', '.join(missing_fields)}")
    else:
        try:
            with st.spinner("Generating your script..."):
                # Initialize the OpenAI client with the API key from secrets
                client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                
                # Prepare features list
                features_text = "\n".join([f"- {feature}" for feature in features]) if features else "- No specific features provided"
                
                prompt = f"""
                # 🎬 SCRIPT BRIEF
                ## App Information
                - **App Name:** {app_name}
                - **Description:** {app_description}
                - **Target Audience:** {target_audience}
                
                ## Key Features
                {features_text}
                
                ## Creative Direction
                - **Tone:** {tone_of_voice}
                - **Format:** {desired_format_trend}
                - **Context:** {contextual_angle if contextual_angle else 'General use case'}
                {f'{chr(10)}## Constraints:{chr(10)}{negative_constraint}' if negative_constraint else ''}
                
                # 🎥 SCRIPT OUTLINE
                
                ## 🎯 0:00-0:03 | HOOK (Grab Attention)
                **Visuals:** [Describe the opening scene, camera angles, and key visual elements]
                **Audio:** [Background music/sound effects]
                **Text Overlay:** [Main hook text]
                **Voiceover/Speaker:** [Dialogue or narration]
                
                ## 💡 0:03-0:08 | PROBLEM (Highlight Pain Point)
                **Visuals:** [Show the problem scenario]
                **Audio:** [Sound effects/music transition]
                **Text Overlay:** [Key pain points]
                **Voiceover/Speaker:** [Emphasize the problem]
                
                ## ✨ 0:08-0:15 | SOLUTION (Introduce App)
                **Visuals:** [App interface/key features in action]
                **Audio:** [Upbeat music]
                **Text Overlay:** [Key features/benefits]
                **Voiceover/Speaker:** [How the app solves the problem]
                
                ## 🚀 0:15-0:25 | DEMO (Show Value)
                **Visuals:** [Step-by-step demo of key features]
                **Audio:** [Highlight key moments with sound effects]
                **Text Overlay:** [Feature names and benefits]
                **Voiceover/Speaker:** [Explain benefits and differentiators]
                
                ## 📢 0:25-0:30 | CTA (Call to Action)
                **Visuals:** [App logo, download buttons, final scene]
                **Audio:** [Music fades, clear CTA]
                **Text Overlay:** [Strong CTA with app name]
                **Voiceover/Speaker:** [Final compelling reason to act]
                
                # 🎨 PRODUCTION NOTES
                
                ## 🎥 Visual Direction
                - **Camera Work:** [Recommended shots, angles, movements]
                - **Lighting:** [Lighting setup suggestions]
                - **Transitions:** [Scene transition ideas]
                
                ## 🔊 Audio Direction
                - **Music:** [Genre/mood suggestions]
                - **Sound Effects:** [Key moments for SFX]
                - **Voiceover:** [Tone and pace guidance]
                
                ## 📝 Additional Notes
                - Keep the pace dynamic and engaging
                - Ensure text is on screen long enough to read (minimum 3 seconds)
                - Highlight key benefits within the first 5 seconds
                - End with a clear, compelling CTA
                
                Make the script engaging, trendy, and perfectly tailored for the {target_audience} audience.
                """
                
                # Make the API call to the fine-tuned model
                try:
                    response = client.chat.completions.create(
                        model="ft:gpt-4.1-nano-2025-04-14:personal:3-content-script-generator:Bvj2a1H5",
                        messages=[
                            {"role": "system", "content": "You are a creative script writer who specializes in creating engaging and effective ad scripts."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=1000
                    )
                except Exception as api_error:
                    st.error(f"Error calling the API: {str(api_error)}")
                    raise
                
                # Extract and display the generated script
                script = response.choices[0].message.content
                
                # Clean up the script formatting
                if script:
                    # Replace escaped newlines with actual newlines
                    script = script.replace('\\n', '\n')
                    # Remove any quotes at the beginning and end if present
                    script = script.strip('"')
                    
                    # Confetti animation on success
                    rain(
                        emoji="✨",
                        font_size=20,
                        falling_speed=5,
                        animation_length=1,
                    )
                    
                    st.markdown("<div class='card fade-in'>", unsafe_allow_html=True)
                    # Display the script in a nice format
                    st.markdown("### 🎬 Your Timeline-Based Script")
                    
                    # Visual Timeline Component
                    st.markdown("""
                    <div class='visual-timeline'>
                        <div class='timeline-header'>📹 Reel Timeline Overview</div>
                        <div class='timeline-container'>
                            <div class='timeline-segment hook'>
                                <div class='segment-time'>0:00-0:03</div>
                                <div class='segment-title'>Hook/Opening</div>
                            </div>
                            <div class='timeline-segment problem'>
                                <div class='segment-time'>0:03-0:08</div>
                                <div class='segment-title'>Problem/Pain</div>
                            </div>
                            <div class='timeline-segment solution'>
                                <div class='segment-time'>0:08-0:15</div>
                                <div class='segment-title'>Solution Intro</div>
                            </div>
                            <div class='timeline-segment demo'>
                                <div class='segment-time'>0:15-0:25</div>
                                <div class='segment-title'>Benefits/Demo</div>
                            </div>
                            <div class='timeline-segment cta'>
                                <div class='segment-time'>0:25-0:30</div>
                                <div class='segment-title'>Call to Action</div>
                            </div>
                        </div>
                        <div class='timeline-progress'>
                            <div class='progress-bar'></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Copy button
                    st.markdown(
                        f"""
                        <div style='text-align: right; margin-bottom: 1rem;'>
                            <button onclick="navigator.clipboard.writeText(`{script}`);" 
                                    style='background: rgba(79, 70, 229, 0.2); 
                                           color: #a5b4fc; 
                                           border: 1px solid rgba(99, 102, 241, 0.3); 
                                           padding: 0.5rem 1.25rem; 
                                           border-radius: 8px; 
                                           cursor: pointer; 
                                           font-weight: 500; 
                                           display: inline-flex; 
                                           align-items: center; 
                                           gap: 0.5rem;
                                           transition: all 0.2s ease;'>
                                📋 Copy Timeline Script
                            </button>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    # Display script in text area - full width
                    st.markdown("</div>", unsafe_allow_html=True)  # Close the card div
                    
                    # Display the script in a clean text area
                    st.text_area(
                        "Timeline Script Content:",
                        value=script,
                        height=400,
                        help="Your timeline-based script with detailed timing and instructions!",
                        label_visibility="visible"
                    )
                    
                    # Share buttons
                    st.markdown("### 🔗 Share Your Creation")
                    st.markdown("""
                    <div style='display: flex; gap: 1rem; margin: 1rem 0;'>
                        <button style='background: rgba(37, 211, 102, 0.1); 
                                     color: #34d399; 
                                     border: 1px solid rgba(52, 211, 153, 0.2); 
                                     padding: 0.5rem 1rem; 
                                     border-radius: 8px; 
                                     cursor: pointer;
                                     transition: all 0.2s ease;'>
                            📱 Share on WhatsApp
                        </button>
                        <button style='background: rgba(29, 161, 242, 0.1); 
                                     color: #60a5fa; 
                                     border: 1px solid rgba(96, 165, 250, 0.2); 
                                     padding: 0.5rem 1rem; 
                                     border-radius: 8px; 
                                     cursor: pointer;
                                     transition: all 0.2s ease;'>
                            🐦 Share on Twitter
                        </button>
                    </div>
                    """, unsafe_allow_html=True)
                    
                else:
                    st.error("❌ Oops! Something went wrong. Please try again.")
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
