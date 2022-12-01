import collections
import re


def what_contains(color, bags_reverse, cont_gold):
    for color in bags_reverse[color]:
        cont_gold.add(color)
        what_contains(color, bags_reverse, cont_gold)


def count_bags(color, bags):
    return sum(number * (1 + count_bags(inner_bag, bags)) for number, inner_bag in bags[color])


def get_bags():
    f = open("day7_input", "r")

    bags = collections.defaultdict(list)  # {given bag : [(1, other bag), (2, another bag)]}
    bags_reverse = collections.defaultdict(set)  # given bag is contained in

    for line in f.readlines():
        color = line.strip().split(" bags contain ")[0]
        bags[color] = []

        if line.split(" contain ")[1] == "no other bags.":
            continue

        for number, inner_bag in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            bags[color].append((int(number), inner_bag))
            bags_reverse[inner_bag].add(color)

    return bags, bags_reverse


def day7():
    bags, bags_reverse = get_bags()

    cont_gold = set()

    what_contains("shiny gold", bags_reverse, cont_gold)
    return len(cont_gold), count_bags("shiny gold", bags)


results = day7()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
