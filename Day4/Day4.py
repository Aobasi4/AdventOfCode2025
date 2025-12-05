# # Link to Day 4 Problem:  https://adventofcode.com/2025/day/4

def create_grid(input_file):
    grid = []
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            grid.append(list(line))
    return grid

# for each position in the grid we need to check the 8 surrounding positions. If there are fewer than 4 positions with a (@) then the 
# position is accesible. return the number of accesible positions in the grid
def Day4_part1(grid):

    grid_length = len(grid)
    accessible_count = 0

    for i in range(grid_length):
        for j in range(len(grid[i])):
            
            if grid[i][j] == '.':
                continue
            # check the 8 surrounding positions
            surrounding_positions = [
                (i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1),           (i, j+1),
                (i+1, j-1), (i+1, j), (i+1, j+1)
            ]
            at_count = 0
            for pos in surrounding_positions:
                x, y = pos
                if 0 <= x < grid_length and 0 <= y < len(grid[i]):
                    if grid[x][y] == '@':
                        at_count += 1
            if at_count < 4:
                accessible_count += 1
             


    return accessible_count

# Now we want to see if more positions are accessible if we remove all @ that were valid in part 1. 
# We can recurively remove @ that are now accessible until no more can be removed, as long as we alter the grid in place when we find an accessible @
def Day4_part2(grid):
    grid_length = len(grid)
    accepted_positions = []

    for i in range(grid_length):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                continue
            # check the 8 surrounding positions
            surrounding_positions = [
                (i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1),           (i, j+1),
                (i+1, j-1), (i+1, j), (i+1, j+1)
            ]
            at_count = 0
            for pos in surrounding_positions:
                x, y = pos
                if 0 <= x < grid_length and 0 <= y < len(grid[i]):
                    if grid[x][y] == '@':
                        at_count += 1
            if at_count < 4:
                accepted_positions.append((i, j))

    # If nothing is removable this round, stop recursion
    if not accepted_positions:
        return 0

    # Remove accepted positions and recurse to find further removals
    for x, y in accepted_positions:
        grid[x][y] = '.'

    return len(accepted_positions) + Day4_part2(grid)


input = create_grid('Day4/Day4Input.txt')
result_part1 = Day4_part1(input)
result_part2 = Day4_part2(input)
print(f"Day 4 Part 1: {result_part1}")
print(f"Day 4 Part 2: {result_part2}")