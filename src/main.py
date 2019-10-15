import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import datetime
from time import sleep
import RPi.GPIO as gpio_config
from ghsTools import ghsTools


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
    cred = credentials.Certificate("./secrets/firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    pulse_amount = 0
    second_diff = 2
    ghsTools().set_monitoring_info(True, second_diff, "Status")
    while True:
        current_time = datetime.datetime.now()
        ref = db.reference("db-info/statuses").get()
        if current_time.hour >= 22 and current_time.minute >= 30 or current_time.hour >= 23 or current_time.hour <= 6:
            for service in pins:
                gpio_config.output(pins[service]["green"], gpio_config.LOW)
                gpio_config.output(pins[service]["red"], gpio_config.LOW)
            pulse_amount = 0
            sleep(60)
        else:
            for service in pins:
                service_status = ref[service]["online"]
                if service_status:
                    gpio_config.output(
                        pins[service]["green"], gpio_config.HIGH)
                    gpio_config.output(pins[service]["red"], gpio_config.LOW)
                else:
                    gpio_config.output(pins[service]["green"], gpio_config.LOW)
                    gpio_config.output(pins[service]["red"], gpio_config.HIGH)
            pulse_amount += 1
            ghsTools().update_pulse(pulse_amount, "Status-Lights")
            sleep(2)


if __name__ == "__main__":
    main()
