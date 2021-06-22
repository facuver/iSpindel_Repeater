from umqtt.robust import MQTTClient
import machine as m
import time

ubidotsToken = "BBFF-bicVhvmk3Gov3FjUTTdhXbFN0oOqRy"
clientID = "test123"
client = MQTTClient("clientID", "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken)
def checkwifi():
    while not sta_if.isconnected():
        time.sleep_ms(500)
        print(".")
        sta_if.connect()
pin13 = m.Pin(13, m.Pin.IN, m.Pin.PULL_UP)
def publish():
    while True:
        checkwifi()
        client.connect()
        lat = 6.2
        lng = -75.56
        var = repr(pin13.value())
        msg = b'{"location": {"value":%s, "context":{"lat":%s, "lng":%s}}}' % (var, lat, lng)
        print(msg)
        client.publish(b"/v1.6/devices/ESP32_EI", msg)
        time.sleep(20)
publish()