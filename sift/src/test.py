from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from core.dependencies import get_gemini_client


gemini_client = get_gemini_client()

ytt_api = YouTubeTranscriptApi()
textFormatter = TextFormatter()

transcript = ytt_api.fetch("36m1o-tM05g")
formatted = textFormatter.format_transcript(transcript)


str_transcript = str(formatted)

# try:
#     open("ytt_transcript","x")
# except FileExistsError:
#     with open("ytt_transcript","w") as file: 
#         file.write(formatted)


response = gemini_client.generate_insights(str_transcript)
print(response)