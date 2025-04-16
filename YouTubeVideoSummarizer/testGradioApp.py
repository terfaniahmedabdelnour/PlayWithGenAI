import gradio as gr 
from YouTubeVideoSummarizer import summarize_youtube_video

import gradio as gr 

gr.close_all()

demo = gr.Interface(fn=summarize_youtube_video,
                    inputs=[gr.Textbox(label="Input YouTube Url to summarize",lines=1)],
                    outputs=[gr.Textbox(label="Summarized text",lines=4)],
                    title="@Project 1: YouTube Script Summarizer",
                    description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE YOUTUBE VIDEO SCRIPT.")
demo.launch(share=True)