#!/usr/bin/python3

import argparse
import serial
import time


parser = argparse.ArgumentParser()
parser.add_argument('action', type=str, help='up or down')
args = parser.parse_args()

ground_floor_down = "d0,d1,d2,d3"
first_floor_down = "d4,d5,d6"
ground_floor_up = "m0,m1,m2,m3"
first_floor_up = "m4,m5,m6"
all_down = ground_floor_down + first_floor_down
all_up = ground_floor_up + first_floor_up
i = 0

def SendCmd(name):
    with serial.Serial("/dev/ttyUSB0", 115200, timeout=1) as arduino:
        time.sleep(0.1)
        if arduino.isOpen():
            try:
                for i in range(5):
                    arduino.write(name.encode())
                    while arduino.inWaiting() == 0: pass
                    if arduino.inWaiting() > 0:
                        arduino.readline().decode('utf-8').rstrip()
                        arduino.flushInput()
                    if i == 1:
                                break
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")

if __name__ == '__main__':
    if args.action == "up":
        SendCmd(ground_floor_up)
    elif args.action == "down":
        SendCmd(all_down)
    else:
        print("wrong action")
