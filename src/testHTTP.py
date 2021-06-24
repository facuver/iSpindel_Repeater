'''
This Example sends harcoded data to Ubidots using the request HTTP
library.

Please install the library using pip install requests

Made by Jose García @https://github.com/jotathebest/
'''

import urequests as requests
import urandom as random
import utime as time

'''
global variables
'''

ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "ESP_TEST"
VARIABLE_LABEL_1 = "temperature"
VARIABLE_LABEL_2 = "humidity"
TOKEN = "BBFF-bicVhvmk3Gov3FjUTTdhXbFN0oOqRy"
DELAY = 1  # Delay in seconds


def post_var(payload, url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}".format(url, device)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Sending data, attempt number: {}".format(attempts))
            req = requests.post(url=url, headers=headers,
                                json=payload)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        print("[INFO] Results:")
        print(req.text)
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))


def main():
    # Simulates sensor values
    sensor_value_1 = random.random() * 100
    sensor_value_2 = random.random() * 100

    # Builds Payload and topíc
    payload = {VARIABLE_LABEL_1: sensor_value_1,
               VARIABLE_LABEL_2: sensor_value_2
              }

    # Sends data
    post_var(payload)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(DELAY)