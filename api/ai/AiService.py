from main import app
import os
import openai


class AiService:
    def __init__(self):
        pass

    @staticmethod
    async def prompt(prompt):
        openai.api_key = "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"
        reply = "Bu sorunuzu yanıtlayamadım. Fakat hızlı cevap alabilmeniz için alanınız ile ilgilenen hocalarımıza email gönderdik en kısa sürede cevabınızı alacaksınız."
        try:
            reply = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            ).choices[0].text
        except:
            print("error: gpt3")
        
        return reply
