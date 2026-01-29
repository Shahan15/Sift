from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from core.dependencies import get_gemini_client


gemini_client = get_gemini_client()

ytt_api = YouTubeTranscriptApi()
textFormatter = TextFormatter()


def get_insights(user_input):
    transcript = ytt_api.fetch(user_input)
    formatted = textFormatter.format_transcript(transcript)

    str_transcript = str(formatted)

    ai_insights = gemini_client.generate_insights(str_transcript)

    with open("ytt_transcript","w") as file: 
        file.write(formatted)

    with open("ytt_insights","w") as file: 
        file.write(ai_insights)

    return ai_insights