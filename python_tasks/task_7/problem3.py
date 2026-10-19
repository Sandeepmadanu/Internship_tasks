
# Problem 3: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
count = 0

for i, char in enumerate(s):
    if char != "SOS"[i % 3]:
        count += 1

print(count)
