
def input_reader(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines

def Day3_part1(lines):
    total = 0
    for line in lines: 

        pivot = 0
        pivot_idx = 0

        for idx, char in enumerate(line[0:len(line)-1]):
            
            if int(char) > pivot:
                pivot = int(char)
                pivot_idx = idx
        
        second_num = 0
        for idx in range(pivot_idx + 1, len(line)):

            if int(line[idx]) > second_num:
                second_num = int(line[idx])
        
        final_str = str(pivot) + str(second_num)
        print(final_str)
        total += int(final_str)
    return total


def max_joltage_for_bank(digits: str, keep: int = 12) -> int:
    """
    Given a string of digits for one battery bank, return the maximum possible
    joltage formed by turning on exactly `keep` batteries (digits), preserving order.
    """
    n = len(digits)
    to_remove = n - keep
    stack = []

    for ch in digits:
        # While we can still remove digits and the last digit in the stack
        # is smaller than the current one, pop it to make number larger.
        while to_remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    # If we still have digits to remove, remove from the end
    if to_remove > 0:
        stack = stack[:-to_remove]

    # Join and convert to int
    return int("".join(stack))


def total_output_joltage(banks, keep: int = 12) -> int:
    return sum(max_joltage_for_bank(bank, keep) for bank in banks)


input = input_reader('Day3/Day3Input.txt')
result_part1 = Day3_part1(input)
print(f"Day 3 Part 1: {result_part1}")
print(f"total out joltage: {total_output_joltage(input, keep=12)}")



# test_input = ['987654321111111',
# '811111111111119',
# '234234234234278',
# '818181911112111']
#test_result_part1 = Day3_part1(test_input)
#print(f"Test Day 3 Part 1: {test_result_part1}")