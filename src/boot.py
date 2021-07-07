# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


import cfg
from cfg import configs 
from oled import screen


print(configs)
 

import wifi




if configs["STA_essid"]:
    screen.print_msg("Connecting to: \n{}".format(configs["STA_essid"]))
    cfg.ip = wifi.do_connect(configs["STA_essid"], configs["STA_password"])
    screen.print_msg("Connected!!")








