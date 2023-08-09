#!/usr/bin/python3
for chr in range(122, 96, -1):
    if chr % 2:
        chr -= 32
    print("{:c}".format(chr), end="")
