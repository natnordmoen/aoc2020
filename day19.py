#!/usr/bin/env python
# inspired by https://gist.github.com/andreypopp/6036fe8dcb891534f15c0d741f68f2f6

def get_rules(f):
    line = f.readline()  # first line
    rules = {}
    while not line == "\n":
        splitted = line.strip().split(":")
        rule_number = splitted[0]
        if '\"' in splitted[1]:
            value = splitted[1].strip()[1]
        elif '|' in splitted[1]:
            sequences = splitted[1].strip().split('|')
            value = [[i for i in seq.strip().split(" ")] for seq in sequences]
        else:
            value = [[i for i in splitted[1].strip().split(" ")]]
        rules[rule_number] = value
        line = f.readline()
    return rules


def get_strings(f):
    strings = []
    for line in f.readlines():
        strings.append(line.strip())
    return strings


def get_input():
    f = open("day19_input", "r")

    rules = get_rules(f)
    strings = get_strings(f)

    return rules, strings


def check_seq(rules, seq, string):
    if not seq:
        yield string
    else:
        rule, *seq = seq
        for string in check(rules, rule, string):
            yield from check_seq(rules, seq, string)


def check_alternatives(rules, alt, string):
    for seq in alt:
        yield from check_seq(rules, seq, string)


def check(rules, rule, string):
    if isinstance(rules[rule], list):
        yield from check_alternatives(rules, rules[rule], string)
    else:
        if string and string[0] == rules[rule]:
            yield string[1:]


def match(rules, string):
    return any(m == '' for m in check(rules, '0', string))


def day19():
    rules, strings = get_input()
    part1 = sum(match(rules, string) for string in strings)
    rules = {**rules, '8': [['42'], ['42', '8']], '11': [['42', '31'], ['42', '11', '31']]}
    part2 = sum(match(rules, string) for string in strings)
    return part1, part2


results = day19()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
