import blinkt
from time import sleep

def main():
    blinkt.clear()
    blinkt.set_all(211, 56, 100, 1.0)
    blinkt.show()
    while True:
        pass
