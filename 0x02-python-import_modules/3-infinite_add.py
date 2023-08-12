#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print(f"{n}")
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(sys.argv[i])
            i += 1
        print(f"{add}")
