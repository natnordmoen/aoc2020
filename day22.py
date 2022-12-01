#!/usr/bin/env python


def get_input():
    f = open("day22_input", "r")
    lines = f.readlines()
    player1 = [int(i) for i in lines[1:len(lines) // 2]]
    player2 = [int(i) for i in lines[(len(lines) // 2) + 2:]]
    return player1, player2


def part1(player1, player2):
    while player1 and player2:
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    return player1 if player1 else player2


def calc_score(winning_hand):
    return sum([i * (index + 1) for index, i in enumerate(winning_hand[::-1])])


def part2(player1, player2):
    already_played = set()

    while player1 and player2:
        hands = (calc_score(player1), calc_score(player2))
        if hands in already_played:
            return calc_score(player1)
        already_played.add(hands)

        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 <= len(player1) and card2 <= len(player2):
            if part2(player1[:card1], player2[:card2]) > 0:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
        elif card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    return calc_score(player1) if player1 else 0 - calc_score(player2)


def day22():
    player1, player2 = get_input()
    part1_winning = calc_score(part1(player1, player2))

    # reset
    player1, player2 = get_input()
    part2_winning = part2(player1, player2)
    return part1_winning, part2_winning


results = day22()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
