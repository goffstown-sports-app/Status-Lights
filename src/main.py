import blinkt
from time import sleep

def main():
    blinkt.clear()
    while True:
        # Green on
        for light in range(7):
            blinkt.set_pixel(light, 0, 250, 0, 0.1)
            sleep(0.5)
        # Green off
        for light in range(7):
            blinkt.set_pixel(light, 0, 250, 0, 0)
            sleep(0.5)
        # Red on
        for light in range(7):
            blinkt.set_pixel(light, 250, 0, 0, 0.1)
            sleep(0.5)
        # Red off
        for light in range(7):
            blinkt.set_pixel(light, 250, 0, 0, 0)
            sleep(0.5)

main()
