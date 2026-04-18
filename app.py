import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

#title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto three images to generate note summary and quizzes")
st.divider()

#sidebar

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the images of your notes", 
         type=['jpg','jpeg','png'],
         accept_multiple_files=True
    )
    
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
        
        
    #image
    if images:
        if len(images)>3:
            st.error("Upload at max three images")
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(images))
            
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
                    
    #difficulty 
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","hard"),
        index = None
    )
    
    if selected_option:
        st.markdown(f"You selected **{selected_option}** as difficulty of your quiz")
    else:
        st.error("You should select a difficulty")
        
    pressed = st.button("Click the button to initiate summary and quiz", 
              type = "primary"
              )
    
if pressed:
    if not images:
        st.error("You should upload at least a image")
    if not selected_option:
        st.error("You should select a difficulty")
        
    if images and selected_option:
        
        #notes
        with st.container(border=True):
            st.subheader("Your Notes")
            
            #this portion will be replaced by API call
            with st.spinner("AI is writing for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)
            
        
        #audio transcript 
        with st.container(border=True):
            st.subheader("Your Audio transcription")
            
            #this portion will be replaced by API call
            with st.spinner("AI is transcripting for you"):
                
                #clearing the markdown
                generated_notes=generated_notes.replace("#","")
                generated_notes=generated_notes.replace("*","")
                generated_notes=generated_notes.replace("-","")
                generated_notes=generated_notes.replace("'","")
                
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)
        
        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz for {selected_option} Difficulty")
            
            #this portion will be replaced by API call
            
            with st.spinner("AI is generating the quizzes"):
                quizzes = quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)
            