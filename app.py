import streamlit as st
import requests
import random  # Task 4: Import random

# --- Task 4: Surprise Me! Configuration ---
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A bioluminescent forest with floating islands",
    "A steampunk clockmaker working on a mechanical dragon",
    "A futuristic city submerged in clear blue ocean water"
]

st.title("AI Image Studio")

# Settings Panel
st.sidebar.header("Settings")
width = st.sidebar.slider("Width", 256, 1024, 512)
height = st.sidebar.slider("Height", 256, 1024, 512)
art_style = st.sidebar.selectbox("Art Style", ["Realistic", "Cyberpunk", "Oil Painting", "3D Render"])

# Task 3: Magic Enhance Toggle
enhance = st.sidebar.checkbox(" ✨ Enable Magic Enhance")

# Generation logic
user_prompt = st.text_input("Enter your prompt:")

# Handle button clicks
if st.button("Generate Image") or st.button(" 🎲 Surprise Me!"):
    
    # Task 4 logic
    if " 🎲 Surprise Me!" in st.session_state.get('last_clicked', ''):
        prompt_to_use = random.choice(surprise_prompts)
    else:
        prompt_to_use = user_prompt

    # Task 3: Magic Enhance logic
    full_prompt = f"{prompt_to_use}, {art_style}"
    if enhance:
        full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

    # Task 1: Fix URL Parameters
    # We use width and height variables here
    url = f"https://image.pollinations.ai/prompt/{full_prompt}?width={width}&height={height}"

    st.image(url)

    # Task 2: File Extension Fix (Dynamic filename)
    image_response = requests.get(url)
    st.download_button(
        label="Download Image",
        data=image_response.content,
        file_name=f"{art_style}_image.png",  # Dynamic filename
        mime="image/png"
    )