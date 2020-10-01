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

            dsum = start1[0] + start2[0] + len1[0] + len2[0]

            for i in range(0, size - 2):
                dsum = dsum + resp[i]

            dsum = dsum & 0xffff

            if (checksum != dsum):
                print("Checksum invalid. {} != {}".format(checksum, dsum))
                continue

            PM1_0_CF1  = pms_value(resp[0], resp[1])
            PM2_5_CF1  = pms_value(resp[2], resp[3])
            PM10_0_CF1 = pms_value(resp[4], resp[5])
            PM1_0_atm  = pms_value(resp[6], resp[7])
            PM2_5_atm  = pms_value(resp[8], resp[9])
            PM10_0_atm = pms_value(resp[10], resp[11])
            air_0_3um  = pms_value(resp[12], resp[13])
            air_0_5um  = pms_value(resp[14], resp[15])
            air_1_0um  = pms_value(resp[16], resp[17])
            air_2_5um  = pms_value(resp[18], resp[19])
            air_5_0um  = pms_value(resp[20], resp[21])
            air_10_0um = pms_value(resp[22], resp[23])
            hcho       = pms_value(resp[24], resp[25])
            temp       = pms_value(resp[26], resp[27])/10
            humi       = pms_value(resp[28], resp[29])/10
            version    = resp[32]
            errorCode  = resp[33]

            print("\nResponse => len: {} bytes, version: {:0>2x}, Error: {:0>2x}".format(size+4, version, errorCode))
            print("+-----------------------------------------------------+")
            print("|  CF=1  | PM1.0 = {:<4d} | PM2.5 = {:<4d} | PM10  = {:<4d} |".format(PM1_0_CF1, PM2_5_CF1, PM10_0_CF1))
            print("|  atm.  | PM1.0 = {:<4d} | PM2.5 = {:<4d} | PM10  = {:<4d} |".format(PM1_0_atm, PM2_5_atm, PM10_0_atm))
            print("|        | 0.3um = {:<4d} | 0.5um = {:<4d} | 1.0um = {:<4d} |".format(air_0_3um, air_0_5um, air_1_0um))
            print("|        | 2.5um = {:<4d} | 5.0um = {:<4d} | 10um  = {:<4d} |".format(air_2_5um, air_5_0um, air_10_0um))
            print("| extra  | hcho  = {:<4d} | temp  = {:<.1f} | humi  = {:<.1f} |".format(hcho, temp, humi))
            print("+-----------------------------------------------------+\n")

        time.sleep(3)

def main():
    print("Run ODYSSEY-uart demo")

    s = serial.Serial(dev_name, baudrate)

    if not s.isOpen():
        s.open()

    try:
        s.write(CMD_PASS)
    except Exception as err:
        print(err)
    finally:
        time.sleep(1)

    
    loop(s)

    s.close()


if __name__ == '__main__':
    main()
