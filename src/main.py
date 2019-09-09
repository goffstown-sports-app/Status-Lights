import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import datetime
from time import sleep
import RPi.GPIO as gpio_config

import database


def main():
    """
    Runs the main file
    :return: None
    """
    pins = {"Scrape-Calendar-Data": {"red": 4, "green": 17},
            "Server-Monitor": {"red": 18, "green": 23}}
    pin_numbers = [4, 17, 18, 23]
    gpio_config.setmode(gpio_config.BCM)
    for pin in pin_numbers:
        gpio_config.setup(pin, gpio_config.OUT)
        gpio_config.output(pin, gpio_config.HIGH)
        sleep(0.2)
        gpio_config.output(pin, gpio_config.LOW)
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    pulse_amount = 0
    second_diff = 2
    database.set_monitoring_info(False, second_diff)
    while True:
        ref = db.reference("db-info/statuses").get()
        for service in pins:
            service_status = ref[service]["online"]
            if service_status:
                gpio_config.output(pins[service]["green"], GPIO.HIGH)
                gpio_config.output(pins[service]["green"], GPIO.LOW)
            else:
                gpio_config.output(pins[service]["green"], GPIO.LOW)
                gpio_config.output(pins[service]["green"], GPIO.HIGH)
        pulse_amount += 1
        database.update_pulse(pulse_amount, "Status-Lights")

if __name__ == "__main__":
    main()
