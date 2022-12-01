#!/usr/bin/env python
import copy


def get_seats():
    f = open("day11_input", "r")
    return [list(n.strip()) for n in f.readlines()]


def count_occupied_adjacent(seats, row_counter, seat_counter):
    first_row = row_counter == 0
    last_row = row_counter == len(seats) - 1
    first_seat = seat_counter == 0
    last_seat = seat_counter == len(seats[0]) - 1

    count_occupied = 0

    if not first_seat and seats[row_counter][seat_counter - 1] == '#':
        count_occupied += 1
    if not last_seat and seats[row_counter][seat_counter + 1] == '#':
        count_occupied += 1
    if not first_row and not first_seat and seats[row_counter - 1][seat_counter - 1] == '#':
        count_occupied += 1
    if not first_row and seats[row_counter - 1][seat_counter] == '#':
        count_occupied += 1
    if not first_row and not last_seat and seats[row_counter - 1][seat_counter + 1] == '#':
        count_occupied += 1
    if not last_row and not first_seat and seats[row_counter + 1][seat_counter - 1] == '#':
        count_occupied += 1
    if not last_row and seats[row_counter + 1][seat_counter] == '#':
        count_occupied += 1
    if not last_row and not last_seat and seats[row_counter + 1][seat_counter + 1] == '#':
        count_occupied += 1

    return count_occupied


def check_left(seats, row_counter, seat_counter):
    i = seat_counter
    while i >= 0:
        if seats[row_counter][i] == 'L':
            return 0
        elif seats[row_counter][i] == '#':
            return 1
        else:
            i -= 1
    return 0


def check_right(seats, row_counter, seat_counter):
    i = seat_counter
    while i <= len(seats[0]) - 1:
        if seats[row_counter][i] == 'L':
            return 0
        elif seats[row_counter][i] == '#':
            return 1
        else:
            i += 1
    return 0


def check_up(seats, row_counter, seat_counter):
    i = row_counter
    while i >= 0:
        if seats[i][seat_counter] == 'L':
            return 0
        elif seats[i][seat_counter] == '#':
            return 1
        else:
            i -= 1
    return 0


def check_down(seats, row_counter, seat_counter):
    i = row_counter
    while i <= len(seats) - 1:
        if seats[i][seat_counter] == 'L':
            return 0
        elif seats[i][seat_counter] == '#':
            return 1
        else:
            i += 1
    return 0


def check_left_up(seats, row_counter, seat_counter):
    r = row_counter
    s = seat_counter
    while r >= 0 and s >= 0:
        if seats[r][s] == 'L':
            return 0
        elif seats[r][s] == '#':
            return 1
        else:
            r -= 1
            s -= 1
    return 0


def check_left_down(seats, row_counter, seat_counter):
    r = row_counter
    s = seat_counter
    while r <= len(seats) - 1 and s >= 0:
        if seats[r][s] == 'L':
            return 0
        elif seats[r][s] == '#':
            return 1
        else:
            r += 1
            s -= 1
    return 0


def check_right_up(seats, row_counter, seat_counter):
    r = row_counter
    s = seat_counter
    while r >= 0 and s <= len(seats[0]) - 1:
        if seats[r][s] == 'L':
            return 0
        elif seats[r][s] == '#':
            return 1
        else:
            r -= 1
            s += 1
    return 0


def check_right_down(seats, row_counter, seat_counter):
    r = row_counter
    s = seat_counter
    while r <= len(seats) - 1 and s <= len(seats[0]) - 1:
        if seats[r][s] == 'L':
            return 0
        elif seats[r][s] == '#':
            return 1
        else:
            r += 1
            s += 1
    return 0


def count_occupied_direction(seats, row_counter, seat_counter):
    first_row = row_counter == 0
    last_row = row_counter == len(seats) - 1
    first_seat = seat_counter == 0
    last_seat = seat_counter == len(seats[0]) - 1

    count_occupied = 0

    if not first_seat:
        count_occupied += check_left(seats, row_counter, seat_counter - 1)
    if not last_seat:
        count_occupied += check_right(seats, row_counter, seat_counter + 1)
    if not first_row:
        count_occupied += check_up(seats, row_counter - 1, seat_counter)
    if not last_row:
        count_occupied += check_down(seats, row_counter + 1, seat_counter)

    if first_row and first_seat:
        count_occupied += check_right_down(seats, row_counter + 1, seat_counter + 1)
    elif last_row and first_seat:
        count_occupied += check_right_up(seats, row_counter - 1, seat_counter + 1)
    elif first_row and last_seat:
        count_occupied += check_left_down(seats, row_counter + 1, seat_counter - 1)
    elif last_row and last_seat:
        count_occupied += check_left_up(seats, row_counter - 1, seat_counter - 1)
    else:
        count_occupied += check_right_down(seats, row_counter + 1, seat_counter + 1)
        count_occupied += check_right_up(seats, row_counter - 1, seat_counter + 1)
        count_occupied += check_left_down(seats, row_counter + 1, seat_counter - 1)
        count_occupied += check_left_up(seats, row_counter - 1, seat_counter - 1)

    return count_occupied


def apply_rules(seats, tolerance, part1):
    new_seats = copy.deepcopy(seats)
    row_counter = 0
    changes = 0

    for row in seats:
        seat_counter = 0
        for seat in row:
            if part1:
                count_occupied = count_occupied_adjacent(seats, row_counter, seat_counter)
            else:
                count_occupied = count_occupied_direction(seats, row_counter, seat_counter)

            if seat == 'L' and count_occupied == 0:
                new_seats[row_counter][seat_counter] = '#'
                changes += 1
            elif seat == '#' and count_occupied >= tolerance:
                new_seats[row_counter][seat_counter] = 'L'
                changes += 1
            seat_counter += 1
        row_counter += 1

    return new_seats, changes


def simulate(seats, tolerance, part1=True):
    while True:
        seats, changes = apply_rules(seats, tolerance, part1)
        if changes == 0:
            break

    occ_total = 0

    for row in seats:
        for seat in row:
            if seat == '#':
                occ_total += 1

    return occ_total


def day11():
    seats = get_seats()

    return simulate(seats, 4, True), simulate(seats, 5, False)


results = day11()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
