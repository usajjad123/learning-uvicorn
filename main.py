## app function from scratch handling the request and response
async def app(scope, _receive, send):
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

## invalid app, does not handle the request and response
async def invalid_app():
    return "Hello, world! noice!"
