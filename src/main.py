import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import datetime
from time import sleep
import RPi.GPIO as gpio_config

# import database

def main():
    """
    Runs the main file
    :return: None
    """
    gpio_config.setmode(gpio_config.BCM)
    gpio_config.setup(17, gpio_config.OUT)
    gpio_config.output(17, gpio_config.HIGH)
    sleep(5)
    gpio_config.output(17, gpio_config.LOW)
    gpio_condig.cleanup()



if __name__ == "__main__":
    main()

