import streamlit as st
from transcribe import transcribe, transcribe_audio
import tempfile
import os
import mimetypes

st.maxUploadSize = 1024

def main():
    st.title('Transcription')
    uploaded_files = st.file_uploader("Choose video or audio files", type=['mp4', 'mp3', 'wav'], accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        st.write(f"File: {uploaded_file.name}")
        file_type = mimetypes.guess_type(uploaded_file.name)[0]

        if 'video' in file_type:
            st.video(uploaded_file)
        elif 'audio' in file_type:
            st.audio(uploaded_file)

    if st.button('Transcribe All'):
        progress_bar = st.progress(0)
        for i, uploaded_file in enumerate(uploaded_files):
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

            st.write(f"Transcription for {uploaded_file.name}: {result}")

            # Delete the temporary file
            os.remove(temp_file_name)

            # Update the progress bar
            progress_bar.progress((i + 1) / len(uploaded_files))

if __name__ == "__main__":
    main()