#!/usr/bin/env python3


def compute_registers(data):
    cycle = []
    register = 1
    cycle.append((0, 0))  # Simplify for later, we always ignore this
    cycle.append((len(cycle), register))

    for line in data:
        if line[0:4] == "addx":
            cycle.append((len(cycle), register))
            register += int(line[5:])
            cycle.append((len(cycle), register))
        elif line[0:4] == "noop":
            cycle.append((len(cycle), register))

    return cycle


def draw_line(cycles):
    line = ""
    offset = 0 - cycles[0][0]
    for cycle in cycles:
        position = cycle[0] + offset
        if position >= (cycle[1] - 1) and position <= (cycle[1] + 1):
            line += "#"
        else:
            line += "."

    return line


def part1(data):
    cycle = compute_registers(data)
    return sum(map(lambda x: x[0] * x[1], cycle[20::40]))


def part2(data):
    output = ""
    cycle = compute_registers(data)
    for i in (1, 41, 81, 121, 161, 201):
        output += draw_line(cycle[i : i + 40]) + "\n"

    return output


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
