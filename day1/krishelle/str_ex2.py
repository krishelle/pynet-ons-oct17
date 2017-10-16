#!/usr/bin/env python
from __future__ import print_function

ip = input("Please enter an IP address: ")
octets = ip.split('.')

try:
    print("{:12}{:12}{:12}{:12}".format(octets[0], octets[1], octets[2], octets[3]))
except IndexError:
    print("Not enough octets in your IP address, please try again.")
