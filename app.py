import asyncio
import websockets
from connect4 import PLAYER1,PLAYER2
import json

async def handler(websocket):
        for player,column,row in [
            (PLAYER1, 3, 0),
            (PLAYER2, 3, 1),
            (PLAYER1, 4, 0),
            (PLAYER2, 4, 1),
            (PLAYER1, 2, 0),
            (PLAYER2, 1, 0),
            (PLAYER1, 5, 0),
        ]:
            event = {
                "type": "play",
                "player": player,
                "column": column,
                "row": row,
            }
            await websocket.send(json.dumps(event)) #for each playing sequence inform the client
            await asyncio.sleep(0.5)
        event = {
            "type": "win",
            "player": PLAYER1
        }
        await websocket.send(json.dumps(event)) #sending winner event 



async def handler1(websocket):
        try:
              async for message in websocket:
                # message = await websocket.recv()
                print(f'message: {message}')
        except websockets.ConnectionClosedOK:
            print('connection was close')

async def main():
    print(f'runninc main...')
    async with websockets.serve(handler,"",8001):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())