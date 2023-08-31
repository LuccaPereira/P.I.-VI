import asyncio
 
import websockets
 
async def handler(websocket, path):
 
    data = await websocket.recv()
 
    reply = f"Data recieved as:  {data}!"
 
    await websocket.send(reply)
 
inicioServer = websockets.serve(handler, "localhost", 8000)
 
asyncio.get_event_loop().run_until_complete(inicioServer)
 
asyncio.get_event_loop().run_forever()