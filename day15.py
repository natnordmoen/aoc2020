#!/usr/bin/env python

def get_input():
    f = open("day15_input", "r")
    return [int(i) for i in f.readline().split(',')]


def take_turns(numbers, turns):
    memory = {}
    for i in range(len(numbers)):
        memory[numbers[i]] = i + 1
    prev_element = numbers[-1]

    for turn in range(len(numbers) + 1, turns + 1):
        number = 0
        if prev_element in memory:
            number = turn - 1 - memory[prev_element]
        memory[prev_element] = turn - 1
        prev_element = number
    return prev_element


def day15():
    numbers = get_input()
    return take_turns(numbers, 2020), take_turns(numbers, 30000000)


results = day15()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
