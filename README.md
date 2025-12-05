# AdventOfCode2025
Advent of Code Challenges for 2025


# Day 1: 
All URLs in Day1.py

Challenges: 

Part 1
- first solution was 128 but the correct answer is higher. 
- I realized I was not counting the cases where steps > 100 correctly.
- The second pass was 526 but this is also too low
- The issue was not handling the case where temp == 100 on the right turn

Part 2
- First pass is 5074 but the correct answer is higher.
- second pass is 7194 but that is to high 
- The issue was not handling the case where steps > 100 correctly again.
- the left logic was incorrect. it needed to only check passing 0 not being equal to 0


# Day 2: 

Part 1:
- I first tried to mathematically calcuate all possible repeating IDs in the range to save on computations. This proved tedious and confusing
- Ended up going with brute force 

Part 2: 
- Was pretty easy. Again it is a classic sliding window on each number. Brute Force, while expensive was easy to solve the problem with!


# Day 3:

Part 1:
- Super easy and strightforward. Just a couple of loops and we're good to go! 

Part 2: 
- Super similar to a Leetcode problem, you want to pop values when they don't make the number bigger. For once Leetcode comes in handy lol


# Day 4: 

Part 1:
- Super simple again, just check every adjacent position and track 

Part 2:
- A little trickier, but easy to solve with Recursion