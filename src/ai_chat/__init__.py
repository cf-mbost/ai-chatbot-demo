import asyncio
from quart import Quart, render_template, websocket
from ai_chat.scripts.open_ai import respond
from ai_chat.broker import Broker


app = Quart(__name__)
broker = Broker()

async def _receive() -> None:
    while True:
        message = await websocket.receive()
        await broker.publish(message)
               
@app.websocket("/ws")
async def ws() -> None:
    try:
        task = asyncio.ensure_future(_receive())
        async for message in broker.subscribe():
            await websocket.send(message)
            await websocket.send(respond(message))
    finally:
        task.cancel()
        await task

@app.route("/")
async def index():
    return await render_template("index.html")


app.run()
