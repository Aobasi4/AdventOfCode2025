# Link to Day 1 Promblem:  https://adventofcode.com/2025/day/1 
# Link to Input Data:  https://adventofcode.com/2025/day/1/input

def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return lines


# The lock starts at position 50
# The input will contain a series of rotations in the format: L/R X
# where L means turn left, R means turn right, and X is the number of positions to turn.
# If the lock goes past position 0, it wraps around to position 99, and vice versa.
# Everytime the lock = 0 exactly, we count 1 point.
# return the total points after processing all rotations.
def lock_rotation(lines):


    start = 50
    counter = 0

    for line in lines:
        direction, steps = line[0], int(line[1:])

        if steps > 100:
            steps = steps % 100
        if direction == 'L':
            temp = start - steps

            if temp < 0: 
                start = 100 + temp
            elif temp == 0:
                counter += 1
                start = temp
            else:
                start = temp
        elif direction == 'R':
            temp = start + steps

            if temp == 100:
                counter += 1
                start = 0
            elif temp > 100:
                start = temp - 100
            else:
                start = temp

    
    return counter

# This time if at any point the lock passses position 0 (not just lands on it), we count 1 point.
def lock_rotation_2(lines):

    start = 50
    counter = 0

    for line in lines: 
        direction, steps = line[0], int(line[1:])

        if steps > 100: 
            counter += steps // 100
            steps = steps % 100
        if direction == 'L':
            temp = start - steps

            if steps > start and start != 0:
                counter += 1

            if temp < 0: 
                start = 100 + temp
            elif temp == 0:
                counter += 1
                start = temp
            else:
                start = temp
        elif direction == 'R':
            temp = start + steps

            if temp == 100:
                counter += 1
                start = 0
            elif temp > 100:
                start = temp - 100
                counter += 1
            else:
                start = temp
        
    return counter

    



input_file_path = 'Day1input.txt'
lines = read_input(input_file_path)
result = lock_rotation(lines)
result2 = lock_rotation_2(lines)
print("The password is:", result)
print("The password for part 2 is:", result2)