#!/usr/bin/env python

def is_valid_part1(occur, letter, password):
    if (password.count(letter)) >= int(occur[0]) and (password.count(letter) <= int(occur[1])):
        return True


def is_valid_part2(positions, letter, password):
    if (password[int(positions[0]) - 1] == letter) ^ (password[int(positions[1]) - 1] == letter):
        return True


def day2():
    f = open("day2_input", "r")
    valid_passwords_part1 = 0
    valid_passwords_part2 = 0
    for line in f.readlines():
        splitted = line.split(' ')
        positions = splitted[0].split('-')  # liste med 2 tall, fra og til
        letter = splitted[1][0]
        password = splitted[2]
        if is_valid_part1(positions, letter, password):
            valid_passwords_part1 += 1
        if is_valid_part2(positions, letter, password):
            valid_passwords_part2 += 1

    print("Part 1: ", valid_passwords_part1)
    print("Part 2: ", valid_passwords_part2)


day2()
