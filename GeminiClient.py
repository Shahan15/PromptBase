
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key : str = os.getenv("GEMINI_API_KEY")
        model = os.getenv('GEMINI_MODEL','gemini-2.5-flash')

        if not api_key:
            raise ValueError(
                "Missing GEMINI_API_KEY"
            )
        
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generateOptimisedPrompt(self,prompt : str) -> str: 
        
        # SENDS PROMPT TO GEMINI TO BE OPTIMISED

        response = self.client.models.generate_content(
            model = self.model,
            contents = prompt
        )

        return response.text

        

        
