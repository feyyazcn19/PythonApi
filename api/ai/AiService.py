from main import app
import os
import openai
from .Response import Response

class AiService:
    def __init__(self):
        pass

    @staticmethod
    async def prompt(prompt):
        openai.api_key = "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"
        response = Response()
        response.responseCode=413
        response.responseMessage="Bu sorunuzu yanıtlayamadım. Fakat hızlı cevap alabilmeniz için alanınız ile ilgilenen hocalarımıza email gönderdik en kısa sürede cevabınızı alacaksınız."
        
        try:
            response.responseMessage = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            ).choices[0].text
            response.responseCode = 200
        except:
            print("error: gpt3")

        return response
