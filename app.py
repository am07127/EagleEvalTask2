import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

st.title("📄 Meeting Transcript Summarizer")
st.write("Drop your meeting transcript below. You'll get a 3-sentence summary.")

# Text area for transcript input
transcript = st.text_area("Paste the meeting transcript here", height=300)

if st.button("Summarize"):
    if not transcript.strip():
        st.warning("Please paste a meeting transcript.")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant that summarizes meeting transcripts in exactly 3 sentences.",
                        },
                        {
                            "role": "user",
                            "content": f"Summarize this transcript in exactly 3 sentences:\n{transcript}",
                        },
                    ],
                    temperature=0.5,
                )
                summary = response.choices[0].message.content
                st.success("Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
