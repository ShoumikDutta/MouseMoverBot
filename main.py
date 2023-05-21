from pyautogui import moveTo
from datetime import datetime
from time import sleep
from random import randint


def main():
    while True:
        x=randint(1,1000)
        y=randint(1,1000)
        moveTo(x,y)
        sleep(1)

        
main()

