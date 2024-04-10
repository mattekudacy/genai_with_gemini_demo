import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=st.secrets['YOUR_API_KEY'])

def main():
    st.title("Audio Summarizer🎤")
    st.write("Upload your podcast or lectures, and I will generate a consice summary of its key points.")

    uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/mp3')

        if st.button("Summarize"):
            summary = generate_summary(uploaded_file)
            st.header("Summary:")
            st.markdown(summary.text)

def generate_summary(audio_file):

    with open("temp.mp3", "wb") as f:
        f.write(audio_file.read())

    sample_file = genai.upload_file(path="temp.mp3")

    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

    system_prompt = "Generate a concise summary of the podcast content."

    response = model.generate_content([system_prompt, sample_file])

    os.remove("temp.mp3")
    genai.delete_file(sample_file.name)

    return response

if __name__ == "__main__":
    main()
