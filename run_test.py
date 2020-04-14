#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   Version 
#   Author: WildfootW
#   GitHub: github.com/WildfootW
#   Copyleft (C) 2020 WildfootW All rights reversed.
#

# usage:
# 1. create a pair of input & output file in test file directory
# 2. pytho3 test.py

import subprocess
import threading # for timeout
from os import listdir
import colorama # for colorful text
import argparse

def timeout(): # for subprocess timeout
    print('timeout')
    exit(3)

def print_test_data(data, style):
    print(style + data.decode("utf-8"))
    print(colorama.Style.RESET_ALL, end = "")

parser = argparse.ArgumentParser(description = """
Test multiple input cases.
z.B. "./test.py -c "g++ ./Problem1/main.cpp" -t ./test_files"
""")
parser.add_argument("-c", "--compile", help = "Compile command. z.B. 'g++ ./main.cpp'", dest = "compile", default = "g++ main.cpp")
parser.add_argument("-t", "--test_files", help = "Testing cases folder. z.B. './tests/'", dest = "test_files_dir", default = "./test_files/")
args = parser.parse_args()

# ininial
test_files_dir = args.test_files_dir if args.test_files_dir[-1:] == "/" else args.test_files_dir + "/"
subprocess.check_call(args.compile, shell=True)

# read file list
input_files = [f for f in listdir(test_files_dir) if f[-6:] == ".input"]
print(input_files)

for input_file in input_files:
    # read sample
    test_name = input_file[:-6]
    test_sample_input = bytes(open(test_files_dir + input_file, "r").read(), "utf-8")
    test_sample_output = b""

    flag_no_output_file = False
    try:
        test_sample_output = bytes(open(test_files_dir + test_name + ".output", "r").read(), "utf-8")
    except FileNotFoundError:
        flag_no_output_file = True

    print(("  " + test_name + "  ").center(80, '='))
    print_test_data(test_sample_input, colorama.Fore.BLUE)
    print_test_data(test_sample_output, colorama.Fore.MAGENTA)

    # run process
    t = threading.Timer(10, timeout)
    proc = subprocess.Popen("./a.out", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    standard_output, standard_err = proc.communicate(test_sample_input)
    t.cancel()

    assert proc.returncode == 0
    assert standard_err == b""
    if standard_output == test_sample_output:
        print("Testing case passed.\n")
    else:
        if not flag_no_output_file:
            print_test_data(standard_output, colorama.Back.RED)
        else:
            print_test_data(standard_output, colorama.Back.YELLOW)

