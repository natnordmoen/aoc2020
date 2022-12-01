#!/usr/bin/env python

def get_input():
    f = open("day1_input", "r")
    numbers = []
    for line in f.readlines():
        numbers.append(int(line))
    return numbers


def part1(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j


def part2(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i * j * k


def day1():
    numbers = get_input()
    return part1(numbers), part2(numbers)


results = day1()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
