from numpy import zeros, nonzero, sum
# top_left is used as tl
# bottom_right is used as br

def turn_on(array, tl, br):
    """Changes state of light to on"""
    for x in range( tl[0], br[0]+1 ):
        for y in range( tl[1], br[1]+1 ):
            array[x][y] = 1

def turn_on_new(array, tl, br):
    """Increases brightness by one"""
    for x in range( tl[0], br[0]+1 ):
        for y in range( tl[1], br[1]+1 ):
            array[x][y] += 1
            
def turn_off(array, tl, br):
    """Changes state of light to off"""
    for x in range( tl[0], br[0]+1 ):
        for y in range( tl[1], br[1]+1 ):
            array[x][y] = 0

def turn_off_new(array, tl, br):
    """Decreases brightness by one with minimum limit zero"""
    for x in range( tl[0], br[0]+1 ):
        for y in range( tl[1], br[1]+1 ):
            array[x][y] -= 1
            if array[x][y] < 0:
                array[x][y] = 0
            
def toggle(array, tl, br):
    """Changes current state of light"""
    for x in range( tl[0], br[0]+1 ):
        for y in range( tl[1], br[1]+1 ):
            if array[x][y] == 1:
                array[x][y] = 0
            else:
                array[x][y] = 1

def toggle_new(array, tl, br):
    """Increase brightness by two"""
    for x in range( tl[0], br[0]+1 ):
        for y in range( tl[1], br[1]+1 ):
            array[x][y] += 2
                
def extract_data(data_line):
    """Extract data out of line to create meaningful information"""
    line = data_line.split()
    length = len(line)
    dst_coordinate = line[-1].split(',')
    src_coordinate = line[-3].split(',')
    command = line[-length: -3]
    for index in range(len(dst_coordinate)):
        dst_coordinate[index] = int(dst_coordinate[index])
    for index in range(len(src_coordinate)):
        src_coordinate[index] = int(src_coordinate[index])
    return [command, src_coordinate, dst_coordinate]    

def read_file(filename):
    with open(filename) as file:
        contents = file.readlines()
    return contents

def install_lights():
    """Creates a 1000*1000 matrix represeting lights in off state"""
    return zeros( (1000,1000), dtype=int )

def count(lights):
    """Returns the number of lights that are in onn state"""
    return len(lights.nonzero()[0])

def operation( lights, command, tl, br ):
    """Evaluates the command and performs appropriate task"""
    if command[0] == "toggle":
        toggle(lights,tl,br)
    elif command[0] == "turn":
        if command[1] == "off":
            turn_off(lights, tl, br)
        elif command[1] == "on":
            turn_on(lights, tl, br)

def operation_new( lights, command, tl, br ):
    """Evaluates the command and performs appropriate task for part two"""
    if command[0] == "toggle":
        toggle_new(lights,tl,br)
    elif command[0] == "turn":
        if command[1] == "off":
            turn_off_new(lights, tl, br)
        elif command[1] == "on":
            turn_on_new(lights, tl, br)
            
def first_star():
    lights = install_lights()
    contents = read_file('Day6.txt')
    for line in contents:
        line = line.strip()
        if line:
            [command, tl, br] = extract_data(line)
            operation(lights, command, tl, br)
    print(count(lights))

def second_star():
    lights = install_lights()
    contents = read_file('Day6.txt')
    for line in contents:
        line = line.strip()
        if line:
            [command, tl, br] = extract_data(line)
            operation_new(lights, command, tl, br)
    print(lights.sum())

if __name__ == "__main__":
    second_star()
