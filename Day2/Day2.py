# Link to Day 2 Problem:  https://adventofcode.com/2025/day/2 
# Link to Input Data:  https://adventofcode.com/2025/day/2/input

def input_reader(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    
    temp = lines[0].split(',')
    lines = temp
    return lines

# the values on the line are comma seperated
# Each line represents an integer range, seperated by a hyphen e.g 12-25
# For each range I need to find the invalid numbers
# An invalid number is one that repeats a subsequence of digits of length n/2 e.g for n=4, 1212 is invalid because 12 repeats
# return the sum of all invalid numbers found in all ranges
def day2_part1(lines):
    invalid_numbers = set()

    for line in lines:
        min, max = map(int, line.split('-')) # min should be 12, max should be 25

        for number in range(min, max + 1):
            num_str = str(number)
            n = len(num_str)

            if n < 2:
                continue # single digit numbers cannot have repeating sequences

            window_size = n // 2

            if num_str[:window_size] == num_str[window_size:]:
                invalid_numbers.add(number)
                continue

    total = 0
    for number in invalid_numbers:
        total += number
    
    return total




# Now, an ID is invalid if it
# is made only of some sequence of digits 
# repeated at least twice. 
# So, 12341234 (1234 two times),
# 123123123 (123 three times), 
# 1212121212 (12 five times), 
# and 1111111 (1 seven times) are all invalid IDs.
def day2_part2(lines):

    invalid_numbers = set()
    for line in lines:
        min, max = map(int, line.split('-')) # min should be 12, max should be 25

        for number in range(min, max + 1):
            if is_invalid_id(number):
                invalid_numbers.add(number)
    
    total = 0
    for number in invalid_numbers:
        total += number
    return total

def is_invalid_id(n: int) -> bool:
    """
    Returns True if the given integer ID is invalid:
    An ID is invalid if its digit string consists of some substring repeated >= 2 times.
    """
    s = str(n)

    # Try every possible substring length that could repeat
    for length in range(1, len(s) // 2 + 1):
        if len(s) % length == 0:  # must divide evenly to repeat
            substring = s[:length]
            if substring * (len(s) // length) == s:
                return True  # invalid because it's a repeated pattern

    return False  # no repeating pattern found → valid
lines = input_reader('Day2/Day2input.txt')
result = day2_part1(lines)
result2 = day2_part2(lines)
print(result)
print(result2)