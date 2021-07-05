import ujson

def read_configs():
    with open("config.json","r") as f:
        conf = ujson.load(f)

    return conf

def update_configs(conf):
    with open("config.json","w") as f:
        ujson.dump(conf,f)
    return conf





configs = read_configs()


time_interval = configs["update_interval"]
token = configs["ubidots_token"]
ip = ""



iSpindels = { 'iSpindelAzul': {'ID': 14914712, 'interval': 10, 'RSSI': -49, 'temperature': 23.4375, 'battery': 3.94682, 'angle': 90.57912, 'gravity': 1.005 , 'name' : 'iSpindelAzul' },
'iSpindelVerde': {'ID': 14914712, 'interval': 10, 'RSSI': -49, 'temperature': 23.4375, 'battery': 3.24682, 'angle': 80.57912, 'gravity': 1.045 , 'name' : 'iSpindelVerde' }}

#'iSpindelAzul': {'ID': 14914712, 'interval': 10, 'RSSI': -49, 'temperature': 23.4375, 'battery': 3.94682, 'angle': 90.57912, 'gravity': 33.85515 , 'name' : 'iSpindelAzul'}
#{"ID": 14914712, "interval": 10, "RSSI": -49, "temperature": 23.4375, "battery": 3.94682, "angl": 90.57912, "gravity": 33.85515 , "name" : "iSpindelAzul"}