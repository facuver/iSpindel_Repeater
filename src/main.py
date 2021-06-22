
import uasyncio as asyncio
import ujson
from ubidots import send_data
from web import app
from cfg import *




#



async def main_loop():
    while True:
        print("Hello")
        await asyncio.sleep(100)


async def update_data():
    while True:
        await asyncio.sleep(int(time_interval))
        if len(iSpindels) != 0:
            for iSpindel in iSpindels:
                send_data(token, iSpindel, ujson.dumps( iSpindels[iSpindel]))
        
        

asyncio.create_task(main_loop())
#asyncio.create_task(update_data())
app.run(port = 80,debug = True)


