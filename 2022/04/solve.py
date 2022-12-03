#!/usr/bin/env python3


def split_groups(line):
    (group_one, group_two) = line.split(",")
    (group_one_start, group_one_end) = group_one.split("-")
    (group_two_start, group_two_end) = group_two.split("-")

    group_one_start = int(group_one_start)
    group_one_end = int(group_one_end)
    group_two_start = int(group_two_start)
    group_two_end = int(group_two_end)

    return group_one_start, group_one_end, group_two_start, group_two_end


def part1(data):
    total = 0
    for line in data:
        group_one_start, group_one_end, group_two_start, group_two_end = split_groups(
            line
        )

        if (group_one_start <= group_two_start and group_one_end >= group_two_end) or (
            group_two_start <= group_one_start and group_two_end >= group_one_end
        ):
            total += 1

    return total


def part2(data):
    total = 0
    for line in data:
        group_one_start, group_one_end, group_two_start, group_two_end = split_groups(
            line
        )

        if (group_one_start <= group_two_end and group_one_end >= group_two_start) or (
            group_two_start <= group_one_end and group_two_end >= group_one_start
        ):
            total += 1

    return total


def main():
    with open("data.txt") as data_file:
        data_string = data_file.read()
    data_lines = data_string.splitlines()
    solution1 = part1(data_lines)
    print(solution1)

    print()

    solution2 = part2(data_lines)
    print(solution2)


if __name__ == "__main__":
    main()
