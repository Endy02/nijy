from machine import Pin
from utime import sleep


if __name__ == "__main__":

    pin = Pin("LED", Pin.OUT)

    print("LED starts flashing...")
    while True:
        pin.toggle()
        sleep(0.5) # sleep 1sec
