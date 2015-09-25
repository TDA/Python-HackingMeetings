__author__ = 'saipc'
import os

def binaryread(filepath):
    with open(filepath, 'rb') as file:
        data = file.read()
        print data


binaryread(r'/Users/schandramouli/Documents/Hacking Meetings/csaw2015/exploitables-100/precision_a8f6f0590c177948fe06c76a1831e650')