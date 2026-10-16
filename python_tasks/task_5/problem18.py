#18.The Minion Game – https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    
    kevin = 0
    stuart = 0
    length = len(string)

    for i in range(length):
        if string[i] in "AEIOU":
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
