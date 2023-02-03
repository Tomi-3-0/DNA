import csv
import sys


def main():

    # Handle command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Empty database file
    filesystem = []

    data = sys.argv[1]
    sequence = sys.argv[2]

    # open data file and add to filesystem list
    with open(data, 'r') as file:
        reader = csv.DictReader(file)
        for r in reader:
            filesystem.append(r)

    # open and read DNA sequence file into a variable
    with open(sequence, 'r') as file:
        dna = file.read()

    # list to check against
    subsequences = list(filesystem[0].keys())[1:]

    # Find longest match of tandem repeats
    matches = {}
    for subsequence in subsequences:
        matches[subsequence] = longest_match(dna, subsequence)

    # Check filesystem for matching profiles
    for name in filesystem:
        match = 0
        for subsequence in subsequences:
            if int(name[subsequence]) == matches[subsequence]:
                match += 1

        # If all subsequences matched
        if match == len(subsequences):
            print(name["name"])
            return

    print("No match")
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

# reference
# https://github.com/tanerijun/cs50_dna/blob/main/dna.py