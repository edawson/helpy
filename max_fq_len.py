import sys

if __name__ == "__main__":

    maxlen = 0
    lcount = 0
    for line in sys.stdin:
        lcount = lcount + 1
        if lcount % 4 == 2:
            l = len(line)
            maxlen = l if l > maxlen else maxlen
    print(maxlen)
