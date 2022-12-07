#!/usr/bin/env python3


def part1(data):
    total_score = 0
    for line in data:
        ...

    return total_score


def part2(data):
    total_score = 0
    for line in data:
        ...

    return total_score


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
