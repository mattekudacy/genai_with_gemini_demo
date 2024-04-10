# Talk Title: Building LLMs with Google AI Studio and Gemini API
By: Cyrus Mante
<br>
Talk Date: April 17, 2024 @ NU Manila 
<br>
[Access slide deck here](https://docs.google.com/presentation/d/1XdJiOpvkTRIT5wa1kVZ0TmFJS4LAVvdJe-RGrU6HWLI/edit?usp=sharing)
## Project Demo
<img src="img/demo1.PNG?raw=true" alt="Demo 1"/> <img src="img/demo2.PNG?raw=true" alt="Demo 2"/> <img src="img/demo3.PNG?raw=true" alt="Demo 3"/>
<br>
## To get started with the project:
1. Clone the project.
```
git clone https://github.com/mattekudacy/genai_with_gemini_demo.git
```
2. Install the requirements. <i> Note: I used Python 3.12 for this project </i>
```
pip install requirements.txt
```

3. Generate your API key through Google AI Studio -> Get API Key -> Create API Key
<img src="img/api.PNG?raw=true" alt="Demo 1"/>

4. Create a new folder in you projects <code>./streamlit</code>, and create a new file called <code>secrets.toml</code>. Create a variable named <code> YOUR_API_KEY </code> and paste your API Key.

```bash
├── gemini_api
│   ├── ./streamlit
│   │   ├── secrets.toml
│   ├── geminibot.py
│   ├── recipai.py
│   ├── summarize_audio.py
│   ├── demo1.jpg
```

6. To run the project:
```
streamlit run geminibot.py
```
```
streamlit run recipai.py
```
```
streamlit run summarize_audio.py
```

7. Enjoy!

Explore more about the Gemini API by reading the [documentation](https://ai.google.dev/docs).

