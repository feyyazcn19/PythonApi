from pydantic import BaseModel

class NewResource(BaseModel):
    search: str
