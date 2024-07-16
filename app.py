import asyncio
import websockets

async def handler(websocket):
    while True: 
        try:
            message = await websocket.recv()
            print(f'message: {message}')
        except websockets.ConnectionClosedOK:
            print('connection was close')
async def main():
    print(f'runninc main...')
    async with websockets.serve(handler,"",8001):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())