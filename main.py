from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

## app function from scratch handling the request and response
async def app_from_scratch(scope, _receive, send):
    assert scope["type"] == "http"

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                (b"content-type", b"text/plain"),
                (b"content-length", b"26"),
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"Hello, world from scratch!",
        }
    )


## app with starlette
async def starlette_route(_request):
    return JSONResponse({'output': 'Hello, world from starlette!'})

app_from_starlette = Starlette(routes=[Route("/", starlette_route)])

## invalid app, does not handle the request and response
async def invalid_app():
    return "Hello, world! noice!"
