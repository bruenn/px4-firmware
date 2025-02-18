#! /usr/bin/python

import serial, time
import subprocess
from subprocess import call, Popen
from argparse import ArgumentParser
import re

def do_test(port, baudrate, test_name):
    databits = serial.EIGHTBITS
    stopbits = serial.STOPBITS_ONE
    parity = serial.PARITY_NONE
    ser = serial.Serial(port, baudrate, databits, parity, stopbits, 100)
    ser.write('\n\n')

    finished = 0
    while finished == 0:
        serial_line = ser.readline()
        print(serial_line.replace('\n',''))

        if "nsh>" in serial_line:
            finished = 1
        time.sleep(0.05)

    ser.write('tests ' + test_name + '\n')

    finished = 0
    success = False
    while finished == 0:
        serial_line = ser.readline()
        print(serial_line.replace('\n',''))

        if test_name + " PASSED" in serial_line:
            finished = 1
            success = True
        elif test_name + " FAILED" in serial_line:
            finished = 1
            success = False

        time.sleep(0.05)

    ser.close()

    return success

def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--device', "-d", nargs='?', default = None, help='')
    parser.add_argument("--baudrate", "-b", dest="baudrate", type=int, help="Mavlink port baud rate (default=57600)", default=57600)
    args = parser.parse_args()


    do_test(args.device, args.baudrate, "autodeclination")
    do_test(args.device, args.baudrate, "bezier")
    do_test(args.device, args.baudrate, "bson")
    do_test(args.device, args.baudrate, "commander")
    do_test(args.device, args.baudrate, "controllib")
    do_test(args.device, args.baudrate, "conv")
    do_test(args.device, args.baudrate, "ctlmath")
    #do_test(args.device, args.baudrate, "dataman")
    do_test(args.device, args.baudrate, "float")
    do_test(args.device, args.baudrate, "hrt")
    do_test(args.device, args.baudrate, "int")
    do_test(args.device, args.baudrate, "IntrusiveQueue")
    do_test(args.device, args.baudrate, "List")
    do_test(args.device, args.baudrate, "mathlib")
    do_test(args.device, args.baudrate, "matrix")
    do_test(args.device, args.baudrate, "microbench_hrt")
    do_test(args.device, args.baudrate, "microbench_math")
    do_test(args.device, args.baudrate, "microbench_matrix")
    do_test(args.device, args.baudrate, "microbench_uorb")
    #do_test(args.device, args.baudrate, "mixer")
    do_test(args.device, args.baudrate, "param")
    do_test(args.device, args.baudrate, "parameters")
    do_test(args.device, args.baudrate, "perf")
    do_test(args.device, args.baudrate, "search_min")
    do_test(args.device, args.baudrate, "sleep")
    do_test(args.device, args.baudrate, "smoothz")
    do_test(args.device, args.baudrate, "time")
    do_test(args.device, args.baudrate, "uorb")
    do_test(args.device, args.baudrate, "versioning")

if __name__ == "__main__":
   main()
