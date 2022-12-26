from .ResourceService import ResourceService
service = ResourceService()

class ResourceController:
    @staticmethod
    async def findResource(search):
        return await (service.searchGoogle(search))
    
    @staticmethod
    async def findSerper(search):
        return await (service.serperSearch(search))