import openai
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import wget 

from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import TextFormatter


#Reading OpenAI API key stored in openai_key.txt in the same folder
with open('openai_key.txt') as f:

    openai.api_key = f.readlines()[0]
    print("oeeeeeee")
    print(type(openai.api_key[0]))



#Prompts openai API for a summarized transcript
def summarize(text):
    st.header("Summary")
    with st.sidebar:
        maxTokens=st.slider('Summary Length', 0, 1000,value=60,step=1)
    with st.spinner('Summarizing the video...⌛'):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text + "Tl;dr",
        temperature=0.7,
        max_tokens=maxTokens,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )

        st.markdown(response['choices'][0]['text'])
        print(response)
    
    st.markdown("Developed with ❤️ by [@dat_rohit](%s)" % "https://github.com/dat-rohit")

    

#Download the subtitles of the provided youtube video
def getSubtitles(videoLink):
    videoID=videoLink[17:]
    transcript=YouTubeTranscriptApi.get_transcript(videoID)
    st.header("Video to summarize")
    download_thumbnail(video_id=videoID)

    return transcript


#Download thumnbail image for provided youtube video
def download_thumbnail(video_id):
    thumbnailurl= 'https://img.youtube.com/vi/'+video_id + '/maxresdefault.jpg'
    thumbnail=wget.download(thumbnailurl)
    st.image(thumbnail)


#Convert the downloaded transcript to a plain text format
def convert(transcript):
    formatter = TextFormatter()
    text_formatted= formatter.format_transcript(transcript) 

    return text_formatted   


if __name__=="__main__":
    yt_link=st.text_input("Insert video link")

    if (len(yt_link)>0):
        print(summarize(convert(getSubtitles(yt_link))))    
