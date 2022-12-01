#!/usr/bin/env python
import sys
from functools import reduce


def read_input():
    f = open("day13_input", "r")
    return int(f.readline()), [(i, int(n)) for i, n in enumerate(f.readline().split(',')) if n != 'x']


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def part2(routes):
    dividers = [route for _, route in routes]
    remainders = [route - i for i, route in routes]
    return chinese_remainder(dividers, remainders)


def part1(timestamp, routes):
    waiting_time = sys.maxsize
    opt_route = 0

    for route in routes:
        rest = timestamp % route  # hvor mange minutter siden bussen har gått

        if route - rest < waiting_time:
            waiting_time = route - rest
            opt_route = route
    return waiting_time * opt_route


def day13():
    timestamp, routes = read_input()  # [(0, 7), (1, 15)]
    p1 = part1(timestamp, [n for _, n in routes])
    p2 = part2(routes)
    return p1, p2


results = day13()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
