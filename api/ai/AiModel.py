from pydantic import BaseModel

class NewAiCommit(BaseModel):
    question: str
