#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the addition of all arguments."""
    import sys
    count = len(sys.argv) - 1
    sum = 0
    for i in range(count):
        sum = sum + int(sys.argv[i + 1])
    print("{}".format(sum))
