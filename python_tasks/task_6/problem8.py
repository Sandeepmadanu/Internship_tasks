
# Problem 8: Tuples
# HackerRank: https://www.hackerrank.com/challenges/python-tuples/problem

import sys

def old_tuple_hash(values):
    mask = (1 << 64) - 1
    acc = 0x345678
    mult = 1000003
    length = len(values)

    for i, value in enumerate(values):
        value_hash = hash(value)
        acc = ((acc ^ value_hash) * mult) & mask
        remaining = length - i - 1
        mult = (mult + 82520 + remaining + remaining) & mask

    acc = (acc + 97531) & mask

    if acc >= (1 << 63):
        acc -= (1 << 64)

    if acc == -1:
        acc = -2

    return acc


if __name__ == "__main__":
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(old_tuple_hash(integer_list))
