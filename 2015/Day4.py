from hashlib import md5

def find_hash(secret_key):
    """Generates hash and compares if the condition is satisfied"""
    min_number = 1
    while True:
        key = secret_key + str(min_number)
        h = md5(key.encode())
        answer = h.hexdigest()
        if answer[:6] == '000000':
            return min_number
        min_number += 1
        
def first_star(puzzle_input):
    """Solution for first star"""
    puzzle_input = puzzle_input.strip()
    if puzzle_input:
        answer = find_hash(puzzle_input)
        print(answer)
    else:
        print('No input given')

def second_star():
    pass

if __name__ == "__main__":
    puzzle_input = 'iwrupvqb'
    first_star(puzzle_input)
