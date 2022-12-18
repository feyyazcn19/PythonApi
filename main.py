from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi
from fastapi.encoders import jsonable_encoder
from typing import Union

app = FastAPI()

from api.resource.ResourceController import ResourceController
from api.resource.ResourceModel import NewResource
from api.ai.AiController import AiController


@app.get("/")
def doc():
    return RedirectResponse("/redoc")

@app.post("/find/resource")
async def find_resource(search : NewResource):
    return  await (ResourceController.findResource(search.search))

@app.post("/ai/commit")
def ai_commit():
    return AiController.getCommit()


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

