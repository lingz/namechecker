import sys
import csv
import json

def main():
    filename = ""
    try:
        filename = sys.argv[1]
    except IndexError:
        print >> sys.stderr, "ERROR: No File passed in"
        print >> sys.stderr, "Usage: python csv_transform.py <FILE_NAME>"
        sys.exit(1)

    with open(filename, 'rb') as jsonfile:
        data = json.loads(jsonfile.read())
        print len(data["data"])
        print u"\n".join(map(lambda x: unicode(x["name"]), data["data"]))

if __name__ == "__main__":
    main()
