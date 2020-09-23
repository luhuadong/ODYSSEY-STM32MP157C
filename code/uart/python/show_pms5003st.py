"""
  Filename: show_pms5003st.py
  Date: 2020-09-23
"""

import sys
import glob
import serial
import time

dev_name = '/dev/ttySTM2'
baudrate = 9600

CMD_READ = bytearray([0x42, 0x4d, 0xe2, 0x00, 0x00, 0x01, 0x71])
CMD_PASS = bytearray([0x42, 0x4d, 0xe1, 0x00, 0x00, 0x01, 0x70])
CMD_ACTI = bytearray([0x42, 0x4d, 0xe1, 0x00, 0x01, 0x01, 0x71])
CMD_STAN = bytearray([0x42, 0x4d, 0xe4, 0x00, 0x00, 0x01, 0x73])
CMD_NORM = bytearray([0x42, 0x4d, 0xe4, 0x00, 0x01, 0x01, 0x74])


def pms_value(hByte, lByte):

    return (hByte << 8 | lByte)


def loop(serial):
    while True:
        serial.write(CMD_READ)

        start1 = serial.read(1)

        if (start1[0] == 0x42):
            start2 = serial.read(1)
            if (start2[0] == 0x4d):
                print("Is a frame")
            else:
                continue
        else:
            continue

        len1 = serial.read(1)
        len2 = serial.read(1)
        size = pms_value(len1[0], len2[0])

        if (size == 36):
            print("Is a response")
            resp = serial.read(size)

            for i in resp:
                print("{:x}".format(i), end=' ')
            print("")

            checksum = pms_value(resp[size-2], resp[size-1])

            dsum = start1[0] + start2[0] + len1[0] + len2[0];

            for i in range(0, size - 2):
                dsum = dsum + resp[i]

            dsum = dsum & 0xffff

            if (checksum != dsum):
                print("Checksum invalid. {} != {}".format(checksum, dsum))
                continue

            print("PM1.0 : {}".format(pms_value(resp[0], resp[1])))
            print("PM2.5 : {}".format(pms_value(resp[2], resp[3])))
            print("PM10  : {}".format(pms_value(resp[4], resp[5])))
            print("PM1.0 : {}".format(pms_value(resp[6], resp[7])))
            print("PM2.5 : {}".format(pms_value(resp[8], resp[9])))
            print("PM10  : {}".format(pms_value(resp[10], resp[11])))
            print("0.3um : {}".format(pms_value(resp[12], resp[13])))
            print("0.5um : {}".format(pms_value(resp[14], resp[15])))
            print("1.0um : {}".format(pms_value(resp[16], resp[17])))
            print("2.5um : {}".format(pms_value(resp[18], resp[19])))
            print("5.0um : {}".format(pms_value(resp[20], resp[21])))
            print("10.0um: {}".format(pms_value(resp[22], resp[23])))
            print("hcho  : {}".format(pms_value(resp[24], resp[25])/1000))
            print("temp  : {}".format(pms_value(resp[26], resp[27])/10))
            print("humi  : {}".format(pms_value(resp[28], resp[29])/10))

        time.sleep(3)

def main():
    print("hello")

    s = serial.Serial(dev_name, baudrate)

    if not s.isOpen():
        s.open()

    try:
        s.write(CMD_ACTI)
    except Exception as err:
        print(err)
    finally:
        time.sleep(0)

    
    loop(s)

    s.close()


if __name__ == '__main__':
    main()
