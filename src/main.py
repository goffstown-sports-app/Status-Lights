import blinkt
from time import sleep
from random import randint

def main():
    blinkt.clear()
    rgbVals = []
    for i in range(8):
        rgbVals.append([0, 0, 0])
    while True:
        LED = randint(0, 7)
        if randint(0, 1) == 0:
            increase = False
        else:
            increase = True
        selectedVal = rgbVals[LED][randint(0, 2)]
        if selectedVal == 250 or not increase:
            selectedVal -= 1
        else:
            selectedVal += 1
        blinkt.set_pixel(LED, rgbVals[LED][0],
                         rgbVals[LED][1], rgbVals[LED][2], 0.1)
        blinkt.show()
        
                

main()
