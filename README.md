# 🖼️ Image-to-Quiz Generator

A Streamlit web app that takes images of your notes and uses **Google Gemini AI** to generate a summary, audio transcription, and quiz.

---

## ✨ Features
- 📷 Upload up to 3 images of your notes
- 📝 AI-generated note summary
- 🔊 Audio transcription of the notes
- 🧠 Quiz generator with Easy / Medium / Hard difficulty

---

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/Arif-AI02/Image-to-Quiz-Generator.git
cd Image-to-Quiz-Generator

### 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up your API key
Create a .env file:
GEMINI_API_KEY=your_gemini_api_key_here
Get your key at: https://aistudio.google.com/

### 5. Run the app
streamlit run app.py

---

## 📦 Dependencies
- streamlit
- google-genai
- Pillow
- gTTS
- python-dotenv

---

## ⚠️ Notes
- Maximum 3 images per session
- Supported formats: .jpg, .jpeg, .png
- Never share your .env file or API key publicly
