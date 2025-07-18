import asyncio
import websockets

async def hello():
    uri="ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name=input ("What's your name?")

        await websocket.send(name)
        print(f"Sent:{name}")

        while True:
            message=await websocket.recv()
            print(f"Received: {message}")

            response=input("Enter you message (or 'quit' to exit):")
            if response.lower()=='quit':
                break
            await websocket.send(response)
            print(f"Sent: {response}")

if __name__=="__main__":
    asyncio.run(hello())