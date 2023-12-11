import streamlit as st
from transcribe import transcribe, transcribe_audio
import tempfile
import os
import mimetypes

def main():
    st.title('Transcription')
    uploaded_file = st.file_uploader("Choose a video or audio file", type=['mp4', 'mp3', 'wav'])

    if uploaded_file is not None:
        file_type = mimetypes.guess_type(uploaded_file.name)[0]

        if 'video' in file_type:
            st.video(uploaded_file)
        elif 'audio' in file_type:
            st.audio(uploaded_file)

        if st.button('Transcribe'):
            # Create a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file_name = temp_file.name

            # Write the uploaded file to the temporary file
            with open(temp_file_name, 'wb') as f:
                f.write(uploaded_file.getbuffer())

            # Transcribe the file
            if 'video' in file_type:
                result = transcribe(temp_file_name, 'base')
            elif 'audio' in file_type:
                result = transcribe_audio(temp_file_name, 'base')

            # Delete the temporary file
            os.remove(temp_file_name)

            st.text_area('Transcription Result:', value=result, height=200)

if __name__ == "__main__":
    main()