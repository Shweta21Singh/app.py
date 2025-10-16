import streamlit as st
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0  # Make results consistent

st.set_page_config(page_title="Language Detector", page_icon="🌍")
st.title("🌍 NLP Language Detection App")
st.markdown("### Paste or type text below to detect the language:")

text_input = st.text_area("Enter your text here 👇", height=150)

if st.button("Detect Language"):
    if text_input.strip():
        try:
            lang_code = detect(text_input)
            # language name mapping
            lang_names = {
                "en": "English", "es": "Spanish", "fr": "French", "de": "German",
                "hi": "Hindi", "ta": "Tamil", "te": "Telugu", "ml": "Malayalam",
                "ru": "Russian", "it": "Italian", "pt": "Portuguese", "bn": "Bengali",
                "ar": "Arabic", "ja": "Japanese", "zh-cn": "Chinese (Simplified)",
                "zh-tw": "Chinese (Traditional)"
            }
            language = lang_names.get(lang_code, lang_code)
            st.success(f"✅ Detected Language: **{language}** (`{lang_code}`)")
        except LangDetectException:
            st.error("⚠️ Could not detect language — please enter longer or clearer text.")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please type or paste some text first.")
