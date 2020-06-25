import sys

if __name__ == "__main__":

    maxlen = 0
    for line in sys.stdin:
        if not line.startswith(">"):
            l = len(line)
            maxlen = l if l > maxlen else maxlen
    print(maxlen)
