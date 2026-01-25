from google import genai
from core.config import settings


class GeminiClient:
    def __init__(self):
        api_key = settings.GEMINI_API_KEY
        model = settings.GEMINI_MODEL


        if not api_key:
            raise ValueError(
                "Missing GEMINI_API_KEY"
            )

        self.instructions = """
        Role: Act as a content analyst and researcher. You will receive a YouTube video transcript. 
        Your goal is to extract high-signal information while ignoring filler, sponsorships, and repetitive speech. 
        Task: Analyze the transcript and provide the following:
        Executive Summary: A 3-sentence overview of the video's core premise and target audience.
        Key Insights & Core Concepts: List the 5-7 most important ideas or arguments presented. For each, provide a brief explanation of why it matters.
        Actionable Takeaways: A bulleted list of specific steps, frameworks, or 'how-to' advice the viewer can implement immediately.
        Data & Evidence: Note any specific statistics, case studies, or expert references mentioned to support the claims.
        Contradictory or Unique Perspectives: Highlight anything the speaker said that goes against 'common wisdom' or is a unique take on the subject.
        The 'Golden Quote': The single most impactful or representative quote from the transcript. 
        Constraints:
        Use Markdown for formatting (headers and bold text).
        If the transcript is messy (no punctuation), infer the structure logically.
        Exclude all mentions of sponsorships or 'like and subscribe' requests.
        """

        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate_insights(self,transcript :str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=transcript,
            config = {'system_instruction' : self.instructions}
        )

        return response.text