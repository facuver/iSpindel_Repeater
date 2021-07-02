
import uasyncio as asyncio

import urequests as requests
from web import app
from cfg import *




async def main_loop():
    while True:
        print("Hello")
        await asyncio.sleep(100)


async def update_data():
    while True:
        await asyncio.sleep(int(time_interval))
        if len(iSpindels) != 0:
            print("Sendind Datas")
            for iSpindel in iSpindels:

                req = requests.post(url = "http://industrial.api.ubidots.com/api/v1.6/devices/{}".format(iSpindel) , headers = {"X-Auth-Token": configs["ubidots_token"] , "Content-Type" : "application/json"} , json=iSpindels[iSpindel])
                await asyncio.sleep(1)
                print(req.text)
        

print(ip)

asyncio.create_task(main_loop())
asyncio.create_task(update_data())
app.run(port = 80,debug = True)


