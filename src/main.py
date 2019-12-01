import blinkt
from time import sleep

def main():
    blinkt.clear()
    blinkt.set_all(20, 181, 14)
    blinkt.show()
    while True:
        pass

main()
