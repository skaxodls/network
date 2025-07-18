import asyncio
import websockets

connected =set()

async def handler(websocket):
    connected.add(websocket)

    try:
        async for message in websocket:
            print(f"Received message: {message}")
            for conn in connected:
                await conn.send(f"Someone said: {message}")
                print(f"sender: {conn}\nmessage: {message}")

    finally:
        connected.remove(websocket)

async def main():
    server=await websockets.serve(handler, "localhost",8765)
    print("WebSocket server started")
    await server.wait_closed()

if __name__=="__main__":
    asyncio.run(main())