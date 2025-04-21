from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

from fastapi import FastAPI

## app function from scratch handling the request and response
async def app_from_scratch(scope, _receive, send):
    assert scope["type"] == "http"

    response_body = b'{"output":"Hello, world from scratch!"}'
    response_length = str(len(response_body)).encode()

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                (b"content-type", b"application/json"),
                (b"content-length", response_length),
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": response_body,
        }
    )


## app with starlette
async def starlette_route(_request):
    return JSONResponse({'output': 'Hello, world from starlette!'})

app_from_starlette = Starlette(routes=[Route("/", starlette_route)])

## app with fastapi
app_from_fastapi = FastAPI()
@app_from_fastapi.get("/")
def fastapi_route():
    return {"output": "Hello, world from fastapi!"}

## invalid app, does not handle the request and response
async def invalid_app():
    return "Hello, world! noice!"
