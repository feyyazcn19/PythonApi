from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from typing import Union
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api.resource.ResourceController import ResourceController
from api.resource.ResourceModel import NewResource
from api.ai.AiModel import NewAiCommit
from api.ai.AiController import AiController


@app.get("/")
def doc():
    return RedirectResponse("/redoc")

@app.post("/find/resource")
async def find_resource(search : NewResource):
    return  await (ResourceController.findResource(search.search))

@app.post("/find/serper")
async def find_serper(search : NewResource):
    return  await (ResourceController.findSerper(search.search))

@app.post("/ai/commit")
async def ai_commit(question : NewAiCommit):
    return await (AiController.getCommit(question.question))


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
