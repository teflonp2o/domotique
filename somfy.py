#!/usr/bin/python3

import argparse
import serial
import time


parser = argparse.ArgumentParser()
parser.add_argument('action', type=str, help='up or down')
args = parser.parse_args()

all_down = "d0,d1,d2,d3"
all_up = "m0,m1,m2,m3"
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
        SendCmd(all_up)
    elif args.action == "down":
        SendCmd(all_down)
    else:
        print("wrong action")
