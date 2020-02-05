from string import ascii_lowercase as al

def property_1(string):
    """Checks property one for nice string"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    occurances = 0
    for vowel in vowels:
        if vowel in string:
            occurances += string.count(vowel)
            if occurances > 2:
                return True
    return False

def property_2(string):
    """Checks property two for nice string"""
    for letter in al:
        pair = letter + letter
        if pair in string:
            return True
    return False

def property_3(string):
    """Checks property three for nice string"""
    pairs = [ 'ab', 'cd', 'pq', 'xy' ]
    for pair in pairs:
        if pair in string:
            return False
    return True

def new_property_1(string):
    """Checks new property one for nice string"""
    length = len(string)
    for offset in range(length-3):
        sub_string = string[offset:offset+2]
        if string.count(sub_string) > 1:
            return True
    return False

def new_property_2(string):
    """Checks new property two for nice string"""
    length = len(string[:-2])
    for offset in range(length):
        sub_string = string[offset:offset+3]
        if sub_string[0] == sub_string[-1]:
            return True
    return False

def is_nice(string):
    """Checks if a string is nice or not"""
    if property_1(string) and property_2(string) and property_3(string):
        return True
    else:
        return False

def is_nice_part2(string):
    """Checks if a string is nice or not for part 2"""
    if new_property_1(string) and new_property_2(string):
        return True
    else:
        return False
    
def read_file(filename):
    with open(filename) as file:
        contents = file.readlines()
    return contents

def first_star():
    """Solution for first star"""
    contents = read_file('Day5.txt')
    answer = 0
    for line in contents:
        line = line.lower().strip()
        if line:
            if is_nice(line):
                answer += 1
        else:
            pass
    print(answer)

def second_star():
    """Solution for second star"""
    contents = read_file('Day5.txt')
    answer = 0
    for line in contents:
        line = line.lower().strip()
        if line:
            if is_nice_part2(line):
                answer += 1
        else:
            pass
    print(answer)

if __name__ == "__main__":
    second_star()
