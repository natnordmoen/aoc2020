#!/usr/bin/env python

def find_seatid(row, seat):
    return (row * 8) + seat


def calculate(ltr, places):
    if len(places) == 1:
        return places
    if ltr in 'FL':
        return places[:len(places) // 2]
    if ltr in 'BR':
        return places[len(places) // 2:]


def find_place(encoded, number):
    places = list(range(number))
    for ltr in list(encoded):
        places = calculate(ltr, places)
    return places[0]


def day5():
    f = open("day5_input", "r")
    seats = []

    # part 1    
    for line in f.readlines():
        row = find_place(line[:7], 128)
        seat = find_place(line[7:], 8)
        seats.append(find_seatid(row, seat))

    # part 2
    missing_seat = [i for i in range(min(seats), max(seats)) if i not in seats][0]

    return max(seats), missing_seat


results = day5()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
