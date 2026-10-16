
# Problem 18: Lists
# Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    L = []

    for _ in range(N):
        command, *args = input().split()
        args = list(map(int, args))

        if command == "insert":
            L.insert(args[0], args[1])
        elif command == "print":
            print(L)
        elif command == "remove":
            L.remove(args[0])
        elif command == "append":
            L.append(args[0])
        elif command == "sort":
            L.sort()
        elif command == "pop":
            L.pop()
        elif command == "reverse":
            L.reverse()