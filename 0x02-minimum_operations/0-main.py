#!/usr/bin/python3
"""0-main.py
Main file for testing the 0-minoperations module
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 8
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 11
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
