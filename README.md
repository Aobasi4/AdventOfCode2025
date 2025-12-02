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