#!/usr/bin/env python

def get_answers():
    f = open("day6_input", "r")
    answers = []
    group = []
    i = 0

    for line in f.readlines():
        if line != '\n':
            group.append(list(line.strip()))
            i += 1
        else:
            answers.append(group)
            i = 0
            group = []
    else:
        answers.append(group)

    return answers


def day6():
    answers = get_answers()

    number_unique = 0
    number_common = 0

    for group in answers:
        number_unique += len(set(group[0]).union(*group))
        number_common += len(set(group[0]).intersection(*group))

    return number_unique, number_common


results = day6()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
