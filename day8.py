#!/usr/bin/env python

def get_instructions():
    f = open("day8_input", "r")
    instructions = {}
    lines = f.readlines()
    i = 0

    for line in lines:
        instructions[i] = [line.strip(), False]
        i += 1

    return instructions, lines


def part1(instructions, lines):
    acc = 0
    i = 0

    while True:
        instr = lines[i].strip().split(' ')
        if instructions[i][1]:
            break
        instructions[i][1] = True
        if instr[0] == 'nop':
            i += 1
        elif instr[0] == 'acc':
            acc += int(instr[1])
            i += 1
        elif instr[0] == 'jmp':
            i += int(instr[1])

    return acc


def day8():
    instructions, lines = get_instructions()  # {0: ('nop +0', False)}
    return part1(instructions, lines)


print("Part 1: ", day8())

