def read_file(filename):
    """Reads file and returns content of the file"""
    with open(filename) as file:
        contents = file.readline()
    return contents.strip()

def first_star():
    houses = [(0,0)]
    content = read_file('Day3.txt')
    current_x = 0
    current_y = 0
    for word in content:
        if word == '^':
            current_y += 1
        elif word == 'v':
            current_y -= 1
        elif word == '<':
            current_x -= 1
        elif word == '>':
            current_x += 1
        houses.append( (current_x,current_y) )

    # Creates a set of all the houses, which eliminates repitition.
    houses = set(houses)
    print(len(houses))

def second_star():
    houses = [(0,0)]
    content = read_file('Day3.txt')
    santa = 1
    [current_x,current_y] = [0,0]
    [santa_x,santa_y] = [0,0]
    [robo_x,robo_y] = [0,0]
    
    for word in content:
        if santa == 1:
            [current_x,current_y] = [santa_x,santa_y]
        else:
            [current_x,current_y] = [robo_x,robo_y]
            
        if word == '^':
            current_y += 1
        elif word == 'v':
            current_y -= 1
        elif word == '<':
            current_x -= 1
        elif word == '>':
            current_x += 1
        houses.append( (current_x,current_y) )

        if santa == 1:
            [santa_x,santa_y] = [current_x,current_y]
            santa *= -1
        else:
            [robo_x,robo_y] = [current_x,current_y]
            santa *= -1

    # Creates a set of all the houses, which eliminates repitition.
    houses = set(houses)
    print(len(houses))


if __name__ == "__main__":
    second_star()
