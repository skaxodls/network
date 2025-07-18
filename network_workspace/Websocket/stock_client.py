import asyncio
import websockets

async def stock_client():
    uri="ws://localhost:62345"
    async with websockets.connect(uri) as websocket:
        print("Connected to stock update server")

        while True:
            data=await websocket.recv()
            print(f"Received stock data: {data}")

if __name__=="__main__":
    asyncio.run(stock_client())
