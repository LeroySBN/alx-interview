#!/usr/bin/python3
"""
module 0-stats: for log parsing
"""
import sys


def print_stats(status_codes, file_size):
    """Prints stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    status_codes = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0}
    file_size = 0
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            file_size += int(data[-1])
            status_codes[data[-2]] += 1
            if count % 10 == 0:
                print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
    print_stats(status_codes, file_size)
