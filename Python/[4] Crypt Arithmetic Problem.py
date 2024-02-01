import itertools

def solve_cryptarithmetic(puzzle):
    # Extracting unique letters from the puzzle
    letters = set(char for char in puzzle if char.isalpha())

    # Number of unique letters
    num_letters = len(letters)

    # Possible digits to assign to letters (0-9)
    digits = range(10)

    # Generating all possible permutations of digits
    for perm in itertools.permutations(digits, num_letters):
        # Mapping digits to letters
        mapping = dict(zip(letters, perm))

        # If the mapping satisfies the puzzle conditions, print it
        if evaluate_puzzle(puzzle, mapping):
            print(mapping)
            return mapping

    print("No Solution Found")

def evaluate_puzzle(puzzle, mapping):
    # Splitting the puzzle into words
    words = puzzle.split()

    # Evaluating the expression
    left_side = ''.join(str(mapping[char]) for char in words[0])
    right_side = ''.join(str(mapping[char]) for char in words[2])
    result = ''.join(str(mapping[char]) for char in words[4])

    # Avoiding leading zeros
    if '0' in (left_side[0], right_side[0], result[0]):
        return False

    # Evaluating the expression
    return int(left_side) + int(right_side) == int(result)

if __name__ == "__main__":
    print("Puzzle Format : Word 1 + Word 2 = Word 3")
    puzzle = input("Enter Puzzle : ") # Example : "HTML + CSSL = TOOL"
    solve_cryptarithmetic(puzzle)
