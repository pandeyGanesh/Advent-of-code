def extract_data(line):
    """Extracts numerical values from given string"""
    list = line.split('x')
    for index in range(len(list)):
        list[index] = int(list[index])
    return list

def get_surface_area(l,w,h):
    """Calculates total surface area"""
    surface_area = 2*l*w
    surface_area += 2*w*h
    surface_area += 2*h*l
    return surface_area

def volume(l,w,h):
    """Calculates volume"""
    return l*w*h

def short_sides(l,w,h):
    """Finds the two shortest sides"""
    sides = [l,w,h]
    sides.sort()
    return sides[:2]

def extra_paper(l,w,h):
    """Calculates the area of shortest side"""
    sides = short_sides(l,w,h)
    return sides[0]*sides[1]

def ribbon(l,w,h):
    """Calculates the smallest perimeter"""
    sides = short_sides(l,w,h)
    return 2*(sides[0]+sides[1])

def read_file(filename):
    """Reads a file and returns a list containing each line"""
    with open(filename) as file:
        contents = file.readlines()
    return contents

def first_star():
    """Solution for first star"""
    contents = read_file('Day2.txt')
    answer = 0
    for line in contents:
        line = line.strip()
        if line:
            [l,w,h] = extract_data(line)
            tsa = get_surface_area(l,w,h)
            extra = extra_paper(l,w,h)
            answer += tsa
            answer += extra
        else:
            pass

    print(answer)

def second_star():
    """Solution for second star"""
    contents = read_file('Day2.txt')
    answer = 0
    for line in contents:
        line = line.strip()
        if line:
            [l,w,h] = extract_data(line)
            vol = volume(l,w,h)
            extra = ribbon(l,w,h)
            answer += vol
            answer += extra
        else:
            pass
    print(answer)
    
if __name__ == "__main__":
    second_star()
