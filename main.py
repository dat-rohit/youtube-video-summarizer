import os
import openai
from youtube_transcript_api import YouTubeTranscriptApi

openai.api_key = "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"




def summarize(originalText):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=originalText,
    temperature=0.7,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    print(response)


def getSubtitles(videoLink):
    videoLink=videoLink[17:]
    transcript=YouTubeTranscriptApi.get_transcript(videoLink)

    return transcript




if __name__=="__main__":
    summarize("Gates was born and raised in Seattle, Washington. In 1975, he and Allen founded Microsoft in Albuquerque, New Mexico. It became the world's largest personal computer software company.[5][a] Gates led the company as chairman and CEO until stepping down as CEO in January 2000, succeeded by Steve Ballmer, but he remained chairman of the board of directors and became chief software architect.[8] During the late 1990s, he was criticized for his business tactics, which have been considered anti-competitive. This opinion has been upheld by numerous court rulings.[9] In June 2008, Gates transitioned to a part-time role at Microsoft and full-time work at the Bill & Melinda Gates Foundation, the private charitable foundation he and his then-wife, Melinda Gates, established in 2000.[10] He stepped down as chairman of the board of Microsoft in February 2014 and assumed a new post as technology adviser to support the newly appointed CEO Satya Nadella.[11] In March 2020, Gates left his board positions at Microsoft and Berkshire Hathaway to focus on his philanthropic efforts including climate change, global health and development, and education.[12]\n\nTl;dr")
