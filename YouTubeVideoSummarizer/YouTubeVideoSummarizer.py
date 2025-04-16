from youtube_transcript_api import YouTubeTranscriptApi
import torch
print("Using device:", "cuda" if torch.cuda.is_available() else "cpu")

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry['text'] for entry in transcript])
    print("Get transctipt function is working well ...")
    return full_text

def extract_video_id(url):
    import re
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
    print("Extract video ID function is working well ...")
    return match.group(1) if match else None

from transformers import pipeline

def summarize_text(text):
    # summarizer = pipeline("summarization", model="facebook/bart-large-cnn",device=-1) #device=-1 ==> force CPU
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)
    
    # Split into chunks if too long
    max_chunk = 500
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""
    for chunk in chunks:
        summary += summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text'] + " "
    print("Summarize text function is working well ...")
    return summary

def summarize_youtube_video(url):
    video_id = extract_video_id(url)
    transcript = get_transcript(video_id)
    summary = summarize_text(transcript)
    print("Summarize text function is working well ...")
    return summary

# Example usage
# video_url = "https://www.youtube.com/watch?v=Ts_I6gcp2Mk"
# print(summarize_youtube_video(video_url))

