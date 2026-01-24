from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

ytt_api = YouTubeTranscriptApi()
textFormatter = TextFormatter()

transcript = ytt_api.fetch("36m1o-tM05g")
formatted = textFormatter.format_transcript(transcript)

try:
    open("ytt_transcript","x")
except FileExistsError:
    with open("ytt_transcript","w") as file: 
        file.write(formatted)

print(formatted)