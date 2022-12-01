#!/usr/bin/env python

facing_dict = {0: 'n', 90: 'e', 180: 's', 270: 'w'}


def get_directions():
    f = open("day12_input", "r")
    return [(n.strip()[0], int(n.strip()[1:])) for n in f.readlines()]


def move_ship_part1(positions, rule, facing):
    if rule[0] == 'F':
        if facing_dict[facing] == 's' or facing_dict[facing] == 'w':
            positions[facing_dict[facing]] -= rule[1]
        else:
            positions[facing_dict[facing]] += rule[1]
    elif rule[0] == 'N':
        positions['n'] += rule[1]
    elif rule[0] == 'S':
        positions['s'] -= rule[1]
    elif rule[0] == 'W':
        positions['w'] -= rule[1]
    elif rule[0] == 'E':
        positions['e'] += rule[1]
    elif rule[0] == 'L':
        facing -= rule[1]
        facing %= 360
    elif rule[0] == 'R':
        facing += rule[1]
        facing %= 360

    return positions, facing


def move_ship_part2(positions_ship, positions_waypoint, distance):
    return positions_ship[0] + (positions_waypoint[0] * distance), positions_ship[1] + (
                positions_waypoint[1] * distance)


def rotate_waypoint_left(waypoint):
    if waypoint[0] >= 0 and waypoint[1] >= 0:
        return -waypoint[1], waypoint[0]
    if waypoint[0] <= 0 and waypoint[1] >= 0:
        return -waypoint[1], waypoint[0]
    if waypoint[0] <= 0 and waypoint[1] <= 0:
        return -waypoint[1], waypoint[0]
    if waypoint[0] >= 0 and waypoint[1] <= 0:
        return -waypoint[1], waypoint[0]


def rotate_waypoint_right(waypoint):
    if waypoint[0] >= 0 and waypoint[1] >= 0:
        return waypoint[1], -waypoint[0]
    if waypoint[0] <= 0 and waypoint[1] >= 0:
        return waypoint[1], -waypoint[0]
    if waypoint[0] <= 0 and waypoint[1] <= 0:
        return waypoint[1], -waypoint[0]
    if waypoint[0] >= 0 and waypoint[1] <= 0:
        return waypoint[1], -waypoint[0]


def move_waypoint(positions_waypoint, rule):
    if rule[0] == 'N':
        return positions_waypoint[0], positions_waypoint[1] + rule[1]
    elif rule[0] == 'S':
        return positions_waypoint[0], positions_waypoint[1] - rule[1]
    elif rule[0] == 'W':
        return positions_waypoint[0] - rule[1], positions_waypoint[1]
    elif rule[0] == 'E':
        return positions_waypoint[0] + rule[1], positions_waypoint[1]
    elif rule[0] == 'L':
        for i in range(rule[1] // 90):
            positions_waypoint = rotate_waypoint_left(positions_waypoint)
        return positions_waypoint
    elif rule[0] == 'R':
        for i in range(rule[1] // 90):
            positions_waypoint = rotate_waypoint_right(positions_waypoint)
        return positions_waypoint


def day12():
    directions = get_directions()
    p = ['n', 'w', 'e', 's']
    positions = {key: 0 for key in p}
    facing = 90

    for d in directions:
        positions, facing = move_ship_part1(positions, d, facing)

    manhattan_dist_1 = abs(positions['n'] + positions['s']) + abs(positions['e'] + positions['w'])

    ship = (0, 0)
    waypoint = (10, 1)

    for d in directions:
        if d[0] == 'F':
            ship = move_ship_part2(ship, waypoint, d[1])
        else:
            waypoint = move_waypoint(waypoint, d)

    manhattan_dist_2 = abs(ship[0]) + abs(ship[1])

    return manhattan_dist_1, manhattan_dist_2


results = day12()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
