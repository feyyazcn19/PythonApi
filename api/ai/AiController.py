from .AiService import AiService
service = AiService()

class AiController:
    @staticmethod
    async def getCommit(prompt):
       return await (service.prompt(prompt))