
# Problem 15: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input().strip()
odd_count = sum(count % 2 for count in Counter(s).values())

print("YES" if odd_count <= 1 else "NO")
