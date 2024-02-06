import itertools

def solve_cryptarithmetic(puzzle):
    letters = set(filter(str.isalpha, puzzle))
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if evaluate_puzzle(puzzle, mapping):
            return mapping
    return None

def evaluate_puzzle(puzzle, mapping):
    words = puzzle.split()
    left, right, result = [int(''.join(str(mapping[char]) for char in word)) for word in words[::2]]
    return left + right == result and all(mapping[word[0]] != 0 for word in words if word[0] in mapping)

if __name__ == "__main__":
    print("Puzzle Format : Word 1 + Word 2 = Word 3")
    puzzle = input("Enter Puzzle : ") # Example : "HTML + CSSL = TOOL"
    print(solve_cryptarithmetic(puzzle) or "No Solution Found")
