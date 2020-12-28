#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def echo():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        ipt = input("input msg: ")

        await websocket.send(ipt)
        print(f"> {ipt}")

        recv = await websocket.recv()
        print(f"< {recv}")

async def loop_echo():
    while True:
        await echo()

asyncio.get_event_loop().run_until_complete(loop_echo())
asyncio.get_event_loop().run_forever()
