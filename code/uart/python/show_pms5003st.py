"""
  Filename: show_pms5003st.py
  Date: 2020-09-23
"""

import sys
import glob
import serial

dev_name = '/dev/ttySTM2'
baudrate = 9600

CMD_READ = bytearray([0x42, 0x4d, 0xe2, 0x00, 0x00, 0x01, 0x71])
CMD_PASS = bytearray([0x42, 0x4d, 0xe1, 0x00, 0x00, 0x01, 0x70])
CMD_ACTI = bytearray([0x42, 0x4d, 0xe1, 0x00, 0x01, 0x01, 0x71])
CMD_STAN = bytearray([0x42, 0x4d, 0xe4, 0x00, 0x00, 0x01, 0x73])
CMD_NORM = bytearray([0x42, 0x4d, 0xe4, 0x00, 0x01, 0x01, 0x74])


def main():
    print("hello")

    s = serial.Serial(dev_name, baudrate)

    if not s.isOpen():
        s.open()

    try:
        s.write(CMD_ACTI)
    except Exception as err:
        print(err)

    s.read(40)
    s.close()


if __name__ == '__main__':
    main()