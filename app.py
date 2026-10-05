import streamlit as st
from gtts import gTTS
import io

# Configure page settings
st.set_page_config(page_title="Text to Voice", page_icon="🔊")
st.title("🔊 Text to Voice Converter")
st.write("Convert entered text into spoken voice using Google Text-to-Speech.")

# Input text area
text_input = st.text_area(
    "Enter text to speak:",
    placeholder="Type the message you want to convert to voice...",
    height=150
)

# Supported language selector
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de"
}
selected_lang = st.selectbox("Choose Language:", options=list(languages.keys()))

# Action button
if st.button("Generate Audio"):
    if not text_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Converting text to speech..."):
            try:
                # Generate voice audio into memory
                tts = gTTS(text=text_input, lang=languages[selected_lang], slow=False)
                audio_buffer = io.BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_buffer.seek(0)

                # Play audio player in UI
                st.success("Audio generated successfully!")
                st.audio(audio_buffer, format="audio/mp3")

                # Audio download button
                st.download_button(
                    label="Download MP3",
                    data=audio_buffer,
                    file_name="voice_output.mp3",
                    mime="audio/mp3"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")