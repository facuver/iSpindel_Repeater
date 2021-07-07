import ujson

def read_configs():
    try:
        with open("config.json","r") as f:
            conf = ujson.load(f)
    except Exception as e:
        print("Error: " , e)
        return {'AP_password': 'test1234', 'AP_essid': 'iSpindel_Repeater', 'update_interval': '600', 'ubidots_token': '', 'STA_essid': '', 'STA_password': ''}

    return conf

def update_configs(conf):
    with open("config.json","w") as f:
        ujson.dump(conf,f)
    return conf





configs = read_configs()




ip = "192.168.4.1"



iSpindels = { }

#'iSpindelAzul': {'ID': 14914712, 'interval': 10, 'RSSI': -49, 'temperature': 23.4375, 'battery': 3.94682, 'angle': 90.57912, 'gravity': 33.85515 , 'name' : 'iSpindelAzul'}
#{"ID": 14914712, "interval": 10, "RSSI": -49, "temperature": 23.4375, "battery": 3.94682, "angle": 90.57912, "gravity": 33.85515 , "name" : "iSpindelAzul" , "temp_units" : "C"}