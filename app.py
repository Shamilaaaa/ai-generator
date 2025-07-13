import streamlit as st
import openai

# 🔐 Enter your API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="AI Image & Caption Generator", layout="centered")
st.title("🧠✨ AI Image + Caption Generator")
st.write("Turn your ideas into visual stories using Generative AI!")

prompt = st.text_input("Enter your idea (e.g., A girl coding under the stars):")

if st.button("Generate"):
    if not prompt:
        st.warning("Please enter a prompt!")
    else:
        # 🧠 Generate Caption
        with st.spinner("Generating caption..."):
            chat_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Write a short, motivational caption for: {prompt}"}],
                max_tokens=50
            )
            caption = chat_response.choices[0].message.content.strip()
        
        # 🎨 Generate Image
        with st.spinner("Generating image..."):
            image_response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = image_response["data"][0]["url"]

        st.image(image_url, caption=caption)
        st.success("Done! Ready to post on LinkedIn ✨")
