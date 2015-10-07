import sys
import csv

def main():
    filename = ""
    try:
        filename = sys.argv[1]
    except IndexError:
        print >> sys.stderr, "ERROR: No File passed in"
        print >> sys.stderr, "Usage: python csv_transform.py <FILE_NAME>"
        sys.exit(1)

    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print row[1] + " " + row[0]

if __name__ == "__main__":
    main()
