import streamlit as st 
from test1 import summarize_youtube_video


st.title("🎥 YouTube Video Summarizer")
st.write("This app summarizes YouTube videos based on their content.")
video_url = st.text_input("Enter Youtube Video URL")

if st.button("Summarize"):
    if video_url:
        summary = summarize_youtube_video(video_url)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter a valid video URL")