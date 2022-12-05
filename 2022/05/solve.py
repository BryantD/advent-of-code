#!/usr/bin/env python3


def build_stacks(data):
    stacks = {}
    i = 0
    while "1" not in data[i]:
        j = 0
        for crate in range(1, len(data[i]), 4):
            if j not in stacks:
                stacks[j] = ""
            if data[i][crate] != " ":
                stacks[j] = stacks[j] + data[i][crate]
            j += 1

        i += 1

    return stacks


def find_top(stacks):
    top_crates = ""

    for stack in stacks:
        if stacks[stack]:
            top_crates += stacks[stack][0]
        else:
            top_crates += " "
    return top_crates


def part1(data):
    stacks = build_stacks(data)

    for line in data:
        if "move" in line:
            (
                move_dummy,
                count,
                from_dummy,
                from_stack,
                to_dummy,
                to_stack,
            ) = line.split(" ")
            count = int(count)
            from_stack = int(from_stack)
            to_stack = int(to_stack)
            from_stack -= 1
            to_stack -= 1
            stacks[to_stack] = stacks[from_stack][0:count][::-1] + stacks[to_stack]
            stacks[from_stack] = stacks[from_stack][count:]

    return find_top(stacks)


def part2(data):
    stacks = build_stacks(data)
    top_crates = ""

    for line in data:
        if "move" in line:
            (
                move_dummy,
                count,
                from_dummy,
                from_stack,
                to_dummy,
                to_stack,
            ) = line.split(" ")
            count = int(count)
            from_stack = int(from_stack)
            to_stack = int(to_stack)
            from_stack -= 1
            to_stack -= 1
            stacks[to_stack] = stacks[from_stack][0:count] + stacks[to_stack]
            stacks[from_stack] = stacks[from_stack][count:]

    return find_top(stacks)


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
