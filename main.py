from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo

ytVideo = "https://www.youtube.com/watch?v=uPxkrGL0l7U"

video_id=ytVideo.split("=")[1]
YouTubeVideo(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

result = ""
for i in transcript:
    
