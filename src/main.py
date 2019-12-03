import blinkt
from time import sleep
from random import randint
from ghsTools import ghsTools
import firebase_admin
import datetime
from firebase_admin import db
from firebase_admin import credentials


def main():
    blinkt.clear()
    blinkt.set_all(0, 250, 0, 1)
    blinkt.show()
    sleep(0.05)
    blinkt.set_all(0, 250, 0, 0)
    blinkt.show()
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
    ghsTools().set_monitoring_info(True, second_diff, "Status-Lights")
    # Add new program here with new light number, thats it!
    program_light_positions = {
        "Scrape-Calendar-Data": 0,
        "Server-Monitor": 1
    }
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour >= 22 and current_time.minute >= 30 or current_time.hour >= 23 or current_time.hour <= 6:
            ref = db.reference("db-info/statuses").get()
            for program in program_light_positions.keys():
                if ref[program]["online"]:
                    blinkt.set_pixel(
                        program_light_positions[program], 0, 250, 0)
                    blinkt.show()
                else:
                    blinkt.set_pixel(
                        program_light_positions[program], 250, 0, 0)
                    blinkt.show()
        else:
            blinkt.set_all(0, 0, 0, 0)
            blinkt.show()
        pulse_amount += 1
        ghsTools().update_pulse(pulse_amount, "Status-Lights")


if __name__ == "__main__":
    main()
