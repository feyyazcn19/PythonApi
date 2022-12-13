from main import app
from .Resource import Resource

class ResourceService(Resource):
    
    def __init__(self):
        self.Resource = Resource
      
    
    def getResource(self):
        self.Resource.searchGoogle()