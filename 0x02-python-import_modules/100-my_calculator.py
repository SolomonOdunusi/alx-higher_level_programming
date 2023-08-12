#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] in ops:
        a = int(argv[1])
        b = int(argv[3])
        op = ops[argv[2]]
        ans = op(a, b)
        print(f"{a} {argv[2]} {b} = {ans}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
