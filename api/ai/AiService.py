from main import app
import os
import openai
from .Response import Response
from decouple import config


class AiService:
    def __init__(self):
        pass

    @staticmethod
    async def prompt(prompt):
        openai.api_key = config("API_GPT_KEY")
        res = Response()

        try:
            res.responseMessage = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            ).choices[0].text
            res.responseCode = 200
        except:
            print("error: gpt3")
            res.responseCode = 413
            res.responseMessage = "Bu sorunuzu yanıtlayamadım. Fakat hızlı cevap alabilmeniz için alanınız ile ilgilenen hocalarımıza email gönderdik en kısa sürede cevabınızı alacaksınız."

        return res
