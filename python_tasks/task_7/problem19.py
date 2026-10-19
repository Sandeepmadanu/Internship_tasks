
# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())

weights = set()
previous = ""
count = 0

for char in s:
    if char == previous:
        count += 1
    else:
        count = 1
        previous = char

    weights.add((ord(char) - ord('a') + 1) * count)

for _ in range(n):
    query = int(input())
    print("Yes" if query in weights else "No")
