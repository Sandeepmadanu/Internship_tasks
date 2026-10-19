
# Problem 4: Funny String
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(
            ord(s[-i]) - ord(s[-i - 1])
        ):
            return "Not Funny"
    return "Funny"


t = int(input())

for _ in range(t):
    print(funnyString(input().strip()))
