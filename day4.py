#!/usr/bin/env python

import re


def is_valid_height(hgt):
    if hgt[-2:] != 'cm' and hgt[-2:] != 'in':
        return False
    elif hgt[-2:] == 'cm':
        return 150 <= int(hgt[0:-2]) <= 193
    elif hgt[-2:] == 'in':
        return 59 <= int(hgt[0:-2]) <= 76
    return False


def is_valid(passport):
    values = []
    for k, v in passport.items():
        if k == 'byr':
            values.append(1920 <= int(v) <= 2002)
        if k == 'iyr':
            values.append(2010 <= int(v) <= 2020)
        if k == 'eyr':
            values.append(2020 <= int(v) <= 2030)
        if k == 'ecl':
            values.append(v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        if k == 'pid':
            values.append(bool(re.fullmatch('\d{9}', v)))
        if k == 'hgt':
            values.append(is_valid_height(v))
        if k == 'hcl':
            values.append(bool(re.fullmatch('#([0-9]*[a-f]*){6}', v)))
    return False not in values


def get_passports():
    f = open("day4_input", "r")
    passports = [{}]
    i = 0
    for line in f.readlines():
        if len(line) != 1:
            pass_values = {}
            for pair in line.strip().split(' '):
                pass_values[pair.split(":")[0]] = pair.split(":")[1]
            passports[i].update(pass_values)
        else:
            i += 1
            passports.append({})
    return passports


def day4():
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = get_passports()
    valid_passports_part1 = []

    for passport in passports:
        if len(set(passport.keys()).intersection(fields)) >= 7:
            valid_passports_part1.append(passport)

    valid_passports_part2 = 0
    for passport in valid_passports_part1:
        if is_valid(passport):
            valid_passports_part2 += 1

    return len(valid_passports_part1), valid_passports_part2


results = day4()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
