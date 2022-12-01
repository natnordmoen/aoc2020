#!/usr/bin/env python

from collections import defaultdict


def make_list_of_rules(values):
    list_of_tuples = [(int(i.split("-")[0]), int(i.split("-")[1])) for i in values]
    list_of_rules = []
    for t in list_of_tuples:
        list_of_rules.extend(list(range(t[0], t[1] + 1)))
    return list_of_rules


def get_rules(f):
    line = f.readline()  # first line
    rules = {}
    while not line == "\n":
        field = line.strip().split(":")[0]
        values = make_list_of_rules(line.strip().split(":")[1].strip().split(" or "))
        rules[field] = values
        line = f.readline()
    return rules


def get_my_ticket(f):
    line = f.readline()  # empty line
    my_ticket = []
    while not line == "\n":
        if not line.startswith("your"):
            my_ticket = [int(i) for i in line.strip().split(",")]
        line = f.readline()
    return my_ticket


def get_nearby_tickets(f):
    f.readline()  # nearby tickets
    nearby_tickets = []
    for line in f:
        nearby_tickets.append([int(i) for i in line.strip().split(",")])
    return nearby_tickets


def get_input():
    f = open("day16_input", "r")

    rules = get_rules(f)
    my_ticket = get_my_ticket(f)
    nearby_tickets = get_nearby_tickets(f)

    return rules, my_ticket, nearby_tickets


def all_values_in_rules(rules):
    return [item for sublist in rules.values() for item in sublist]


def delete_used_field(column_to_rule, field):
    for k, v in column_to_rule.items():
        if field in v:
            v.remove(field)
    return column_to_rule


def filter_rules(column_to_rule):
    final_mapping = {}  # colNumber : fieldName
    while len(column_to_rule.keys()) != 0:
        for k, v in column_to_rule.copy().items():
            if len(v) == 1:
                final_mapping[k] = v[0]
                del column_to_rule[k]
                column_to_rule = delete_used_field(column_to_rule, v[0])
    return final_mapping


def part2(rules, tickets):
    columns = len(tickets[0])
    column_to_rule = defaultdict(lambda: [])
    for c in range(columns):
        for field, rule in rules.items():
            for ticket in tickets:
                if ticket[c] not in rule:
                    break
            else:
                column_to_rule[c].append(field)
    field_mapping = filter_rules(column_to_rule)
    return {v: k for k, v in field_mapping.items()}  # fieldName : fieldNumber


def part1(rules, nearby_tickets):
    all_values = all_values_in_rules(rules)
    invalid_values = []
    valid_tickets = []

    for ticket in nearby_tickets:
        ticket_is_valid = True
        for value in ticket:
            if value not in all_values:
                invalid_values.append(value)
                ticket_is_valid = False
        if ticket_is_valid:
            valid_tickets.append(ticket)

    return sum(invalid_values), valid_tickets


def day16():
    rules, my_ticket, nearby_tickets = get_input()
    error_rate, valid_tickets = part1(rules, nearby_tickets)
    field_map = part2(rules, valid_tickets)

    departure_values = 1
    for k, v in field_map.items():
        if k.startswith('departure'):
            departure_values *= my_ticket[v]

    return error_rate, departure_values


results = day16()

print("Part 1: ", results[0])
print("Part 2: ", results[1])
