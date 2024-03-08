import json
import sys

if __name__ == "__main__":

    with open(sys.argv[1], "r") as ifi:
        print(json.dumps(json.loads(ifi.read())).replace(r'\"', '"').replace('"', r'\"'))
