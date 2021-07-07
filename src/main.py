
import uasyncio as asyncio


import urequests as requests
from web import app
from cfg import *
import gc

from usys import exit

from oled import screen


async def main_loop():
    while True:
        print("Hello")
        
        await asyncio.sleep(10)


async def update_screen():
    while True:
        if len(iSpindels):
            for i in iSpindels:
                screen.update(iSpindels[i])
                #print(i)
                await asyncio.sleep(5)
        else:
            screen.print_msg("No iSpindels \n{}".format(ip))
            
        await asyncio.sleep(0)

async def update_data():
    while True:
        await asyncio.sleep(int(configs["update_interval"]))
        if len(iSpindels) != 0:
            print("Sendind Datas")
            for iSpindel in iSpindels:

                req = requests.post(url = "http://industrial.api.ubidots.com/api/v1.6/devices/{}".format(iSpindel) , headers = {"X-Auth-Token": configs["ubidots_token"] , "Content-Type" : "application/json"} , json=iSpindels[iSpindel])
                await asyncio.sleep(1)
                print(req.text)
        

async def gb_col():
    while True:

        gc.collect()
        gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
        print(gc.mem_free())
        await asyncio.sleep(10)

print(ip)

main_task = asyncio.create_task(main_loop())
screen_task = asyncio.create_task(update_screen())
update_task = asyncio.create_task(update_data())
asyncio.create_task(gb_col())
app.run(port = 80,debug = True)


