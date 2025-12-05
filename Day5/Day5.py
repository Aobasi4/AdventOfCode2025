# Link to Day 5 Problem:  https://adventofcode.com/2025/day/5


def input_reader(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    
    empty_space = lines.index('')

    ranges = lines[0:empty_space]
    values = lines[empty_space + 1:]

    return ranges, values

def Day5_part1(ranges, values):
    total = 0

    for line in values:
        number = int(line)
        if any(int(r.split('-')[0]) <= number <= int(r.split('-')[1]) for r in ranges):
            total += 1
    return total

def Day5_part2(ranges):
    # Parse ranges into list of (start, end) tuples
    intervals = []
    for line in ranges:
        start, end = map(int, line.split('-'))
        intervals.append((start, end))

    if not intervals:
        return 0

    # Sort by start
    intervals.sort(key=lambda x: x[0])

    # Merge overlapping (or contiguous) intervals and sum their lengths
    total = 0
    cur_start, cur_end = intervals[0]

    for s, e in intervals[1:]:
        if s <= cur_end + 1:
            # Overlaps or contiguous: extend current interval
            cur_end = max(cur_end, e)
        else:
            # Disjoint interval: add length of current, start new
            total += (cur_end - cur_start + 1)
            cur_start, cur_end = s, e

    # Add the last interval
    total += (cur_end - cur_start + 1)
    return total

    


ranges, values = input_reader('Day5/Day5Input.txt')
print(Day5_part1(ranges, values))
print(Day5_part2(ranges))