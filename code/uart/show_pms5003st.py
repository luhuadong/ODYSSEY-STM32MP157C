"""
  Filename: show_pms5003st.py
  Date: 2020-09-23
"""

import sys
import glob
import serial

dev_name = '/dev/ttySTM2'
baudrate = 9600


def main():
    print("hello")

    s = serial.Serial(dev_name, baudrate)

    try:
        s.open()
    except Exception as e:
        print("Open {} failed.".format(dev_name))
        print("Reason: {}".format(str(e)))

    s.read(40)
    s.close()


if __name__ == '__main__':
    main()