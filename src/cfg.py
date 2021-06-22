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

