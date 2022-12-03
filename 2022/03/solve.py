#!/usr/bin/env python3


def find_priority(character):
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return priority.index(character) + 1


def part1(data):
    total = 0
    for line in data:
        first = line[: int(len(line) / 2)]
        second = line[int(len(line) / 2) :]
        total += find_priority(set.intersection(set(first), set(second)).pop())

    return total


def part2(data):
    total = 0
    for group in range(0, len(data), 3):
        total += find_priority(
            set.intersection(
                set(data[group]), set(data[group + 1]), set(data[group + 2])
            ).pop()
        )

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
