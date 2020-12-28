#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def echo(websocket, path):
    recv = await websocket.recv()
    print(f"< {recv}")

    resp = recv
    await websocket.send(resp)
    print(f"> {resp}")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
