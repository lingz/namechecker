from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys
import random


# threshold for a name match, feel free to change

def main():
    print "\nYou will be asked for the 'match threshold', how similar names must be to match You can play with this value and see. Try starting with 80 if you don't know"

    MATCH_THRESHOLD = input("\nPlease enter the match threshold (0-100): ")
    allowed_filename = ""
    to_check_filename = ""
    try:
        allowed_filename = sys.argv[1]
        to_check_filename = sys.argv[2]
    except IndexError:
        print >> sys.stderr, "ERROR: No File passed in"
        print >> sys.stderr, "Usage: python checker.py <ALLOWED_FILENAME> <TO_CHECK_FILENAME>"
        sys.exit(1)

    print "Reading allowed names from: %s" % allowed_filename
    print "Reading names to check from: %s" % to_check_filename

    allowed_names = []
    to_check_names = []

    with open(allowed_filename, 'r') as names_file:
        for name in names_file:
            allowed_names.append(name.strip())

    with open(to_check_filename, 'r') as names_file:
        for name in names_file:
            to_check_names.append(name.strip())

    random.shuffle(to_check_names)

    print allowed_names
    print to_check_names

    unmatched = []

    # Simple algorthim
    # For each name, mark it as checked if it matches
    # above the threshold. And delete it from both lists
    print "\nBeginning Matching:"
    for to_check_name in to_check_names:
        print to_check_name + " ...",
        if len(allowed_names) == 0:
            print "FAIL"
            unmatched.append((to_check_name, []))
            continue
        res = process.extract(to_check_name, allowed_names, limit=3, scorer=fuzz.partial_ratio)

        print res[0][1],
        if len(res) > 0 and res[0][1] > MATCH_THRESHOLD:
            print "MATCH"
            allowed_names.remove(res[0][0])
        else:
            print "FAIL"
            unmatched.append((to_check_name, map(lambda x: x[0], res)))

    print_result(allowed_names, unmatched)

    print("Would you like help manually approving/rejecting the unmatched names?")
    want_help = input("1 = Yes, 2 = No: ") == 1

    if not want_help:
        return

    print("\nStarting Manual Matching")
    still_unmatched = []
    # Iterate through the list and offer suggestions
    for unmatched_res in unmatched:
        print("")
        print("Name: " + unmatched_res[0])
        print("Top matches: " + ", ".join(unmatched_res[1]))
        print("Do you want to approve or reject this name?")
        approved = input("1 = Approve, 2 = Reject: ") == 1
        if not approved:
            still_unmatched.append(unmatched_res)

    print_result(None, still_unmatched)

def print_result(allowed_names, unmatched):
    if allowed_names and len(allowed_names) > 0:
        print "\nThe following allowed names are not in the group:"
        print "\n".join(allowed_names)

    print "\nThe following names did not appear on the approve list:"
    print "\n".join(map(lambda x: x[0], unmatched))

    print "\nResult:"
    print "%d name(s) on the list did not match to approved names" % len(unmatched)
    if allowed_names:
        print "%d allowed name(s) are not on the list\n" % len(allowed_names)


if __name__ == "__main__":
    main()
