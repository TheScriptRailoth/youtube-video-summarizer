from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo

ytVideo = "https://www.youtube.com/watch?v=uPxkrGL0l7U"

video_id=ytVideo.split("=")[1]
YouTubeVideo(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

result = ""
for i in transcript:
    result+= ' '+i['text']
totalLength =len(result)

summarizer = pipeline('summarization')

num_iters = int(len(result)/1000)
summarized_text =[]
for i in range(0, num_iters +1):
    start = 0
    start = i*1000
    end = (i+1)*1000

    out = summarizer(result[start:end])
    out=out[0]
    out=out['summary_text']
    summarized_text.append(out)

summarizedLength = len(str(summarized_text))
SummarizedText = str(summarized_text)