import streamlit as st
import google.generativeai as genai
import PIL.Image

genai.configure(api_key=st.secrets['YOUR_API_KEY'])

def main():
    st.title("RecipAI🍔")
    st.write("RecipAI is a recipe generator that generates recipes based on the image and prompt you provide. It uses the GeminiAPI to generate the recipe.")

    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = PIL.Image.open(uploaded_file)
        
        st.image(img, caption='Uploaded Image.', use_column_width=True)
        
        inp = st.text_input("Enter your prompt")
        system_prompt = f"You are a chef in a restaurant. You are tasked with this task: {inp}. Add a bit of history to the dish. Provide the dish name, ingredients in markdown table, and preparations to make the dish possible"

        if st.button("Generate"):
            model = genai.GenerativeModel('gemini-pro-vision')
            response = model.generate_content([system_prompt, img])

            st.markdown(response.text)

if __name__ == "__main__":
    main()

