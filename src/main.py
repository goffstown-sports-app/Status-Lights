import blinkt
from time import sleep

def main():
    blinkt.clear()
    blinkt.set_all(20, 181, 14)
    blinkt.show()
    blinkt.set_clear_on_exit(value=True)
    while True:
        pass

main()
