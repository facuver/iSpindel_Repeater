import utime as time 
import network 

from cfg import configs 

def do_connect(ssid, pwd, hard_reset=True):
    interface = network.WLAN(network.STA_IF)
    print("Connecting")
    # Stage zero: if credential are null disconnect
    if not ssid :
        print('Disconnecting')
        interface.active(False)
        return "192.168.4.1"

    # Stage one: check for default connection
    for t in range(0, 120):
        if interface.isconnected():
            print('Oh Yes! Get connected')
            return interface.ifconfig()[0]
        time.sleep_ms(200)
        # Stage two: if not yet connected and after a hard reset activate and connect
        if t == 60 and hard_reset:
            interface.active(True)
            interface.connect(ssid, pwd)

    # No way we are not connected
    print('Cant connect to ', ssid , ". Startin AP")
    interface.active(False)
    
    return interface.ifconfig()[0]








ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid=configs["AP_essid"], authmode = 4 , password = configs["AP_password"]) # set the ESSID of the access point

ap.config(max_clients=10) # set how many clients can connect to the network
ap.active(True)         # activate the interface

