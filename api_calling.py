from google import genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS
import streamlit as st


#loading the environemnt variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#initializing client
client = genai.Client(api_key = my_api_key)

# note generator 
def note_generator(images):
    
    prompt = """ Summarize the picture in the note format at max 100 words, make sure add necessary markdown to differentiate different section"""
    
    response = client.models.generate_content(
        model = ("gemini-3-flash-preview"),
        contents = [images,prompt]
    )
    
    return response.text


def audio_transcription(text):
    speech = gTTS(text,lang='en',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generator(images,difficulty):
    prompt = f" generate three quizzes based on {difficulty}. make sure to add mardown to differenciate the options. Add correct answers after the quiz "
    
    response = client.models.generate_content(
        model = ("gemini-3-flash-preview"),
        contents = [images,prompt]
    )
    
    return response.text