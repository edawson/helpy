import json
import sys

if __name__ == "__main__":

    with open(sys.argv[1], "r") as ifi:
        print(ifi.read().replace(r'\"', '"').replace('"', r'\"').replace("\n", "\\n"))
