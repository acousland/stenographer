import streamlit as st
from transcribe import transcribe


st.title('Video Transcription')
uploaded_file = st.file_uploader("Choose a video file", type=['mp4'])

if uploaded_file is not None:
    st.video(uploaded_file)
    if st.button('Transcribe'):
        result = transcribe(uploaded_file, 'base')
        st.text_area('Transcription Result:', value=result, height=200)