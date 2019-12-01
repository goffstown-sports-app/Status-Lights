import blinkt
from time import sleep
from random import randint

def main():
    blinkt.clear()
    blinkt.set_all(0, 250, 0, 1)
    sleep(0.01)
    blinkt.set_all(0, 250, 0, 0)
        
                

main()
