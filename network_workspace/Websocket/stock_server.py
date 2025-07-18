import asyncio
import websockets
import json
import random

stocks={
    "AAPL":150.0,
    "GOOGL":2800.0,
    "MSFT":300.0,
    "AMZN":3300.0
}

connected=set()

async def stock_update():
    while True:
        for stock in stocks:
            change=random.uniform(-5,5)
            stocks[stock]+=change

        data=json.dumps(stocks)

        if connected:
            await asyncio.wait([asyncio.create_task(client.send(data)) for client in connected])
            await asyncio.sleep(1)

async def handler(websocket, path):
    connected.add(websocket)
    try:
        await websocket.send(json.dumps(stocks))
        async for message in websocket:
            pass
    finally:
        #클라이언트 연결이 종료되면 집합에서 제거
        connected.remove(websocket)


async def main():
    asyncio.create_task(stock_update())

    server=await websockets.serve(handler, "localhost", 62345)
    print("Stock update server started")
    await server.wait_closed()

if __name__=="__main__":
    asyncio.run(main())
