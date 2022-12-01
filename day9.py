#!/usr/bin/env python

import itertools


def convert_to_int(lines):
    numbers = []
    for i in lines:
        numbers.append(int(i.strip()))
    return numbers


def get_preamble(pre_length):
    f = open("day9_input", "r")
    lines = f.readlines()
    numbers = convert_to_int(lines)
    i = 0
    preamble = []

    for n in numbers:
        if i < pre_length:
            preamble.append(n)
            i += 1
        else:
            break

    return preamble, numbers


def check_sum(preamble, target):
    for numbers in itertools.combinations(preamble, 2):
        if sum(numbers) == target:
            preamble = preamble[1:]
            preamble.append(target)
            return True, preamble
    return False, []


def part2(numbers, target):
    current_sum = 0
    cur_list = []
    i = 0

    while i < len(numbers):
        if current_sum == target:
            return cur_list
        if current_sum < target:
            current_sum += numbers[i]
            cur_list.append(numbers[i])
        elif current_sum > target:
            current_sum -= cur_list[0]
            cur_list.pop(0)
            continue
        i += 1

    return []


def part1(preamble, numbers, pre_length):
    invalid_number = 0

    for number in numbers[pre_length:]:
        is_sum, new_preamble = check_sum(preamble, number)
        if is_sum:
            preamble = new_preamble
            continue
        else:
            invalid_number = number
            break

    return invalid_number


def day9():
    pre_length = 25
    preamble, numbers = get_preamble(pre_length)

    # part 1
    invalid_number = part1(preamble, numbers, pre_length)

    # part 2
    contigious_list = part2(numbers, invalid_number)
    sum_cont_list = min(contigious_list) + max(contigious_list)

    return invalid_number, sum_cont_list


results = day9()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
