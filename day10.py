#!/usr/bin/env python
from collections import defaultdict


def get_jolts():
    f = open("day10_input", "r")
    return sorted([int(n.strip()) for n in f.readlines()])


def part2(jolts):
    cost_jolt = defaultdict(lambda: 0)
    cost_jolt[0] = 1

    for a in jolts:
        cost_jolt[a] = cost_jolt[a - 3] + cost_jolt[a - 2] + cost_jolt[a - 1]

    return cost_jolt[jolts[-1]]


def part1(jolts):
    current = 0
    differences = {}

    for i in jolts:
        diff = i - current
        if diff in differences:
            differences[diff] += 1
        else:
            differences[diff] = 1
        current = i

    differences[3] += 1 # legge til build-in adapter

    return differences[1] * differences[3]


def day10():
    jolts = get_jolts()
    return part1(jolts), part2(jolts)


results = day10()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
