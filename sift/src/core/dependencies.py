from services.gemini_client import GeminiClient

gemini_client = None

def get_gemini_client() -> GeminiClient:
    global gemini_client

    if gemini_client is None:
        print("---INITIALISING NEW GEMINI CLIENT OBJECT---")
        gemini_client = GeminiClient()
    return gemini_client
