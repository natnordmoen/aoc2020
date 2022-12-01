#!/usr/bin/env python

def count_trees(right, down):
    trees = 0
    index_line = 0
    index_position = 0

    # lese inn fila som 2d array
    with open("day3_input") as f:
        lines = [list(line.strip()) for line in f]

    # forlenge linjer til maks stoerrelse
    lines = [line * (len(lines) * right) for line in lines]

    # telle traer    
    while index_line < len(lines):
        if lines[index_line][index_position] == '#':
            trees += 1
        index_line += down
        index_position += right
    return trees


def day3():
    slopes_part1 = [3, 1]
    print("Part 1: ", count_trees(slopes_part1[0], slopes_part1[1]))
    slopes_part2 = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    total_trees = 1
    for i in slopes_part2:
        total_trees *= count_trees(i[0], i[1])
    print("Part 2: ", total_trees)


day3()
