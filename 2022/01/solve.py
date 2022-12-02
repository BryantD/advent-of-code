#!/usr/bin/env python3


def part1(data):
    biggest_elf_calories = 0
    current_elf_calories = 0

    for line in data:
        if line == "":
            if current_elf_calories > biggest_elf_calories:
                biggest_elf_calories = current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

    return biggest_elf_calories


def part2(data):
    current_elf_calories = 0
    biggest_three_elf_calories = [0, 0, 0]

    for line in data:
        if line == "":
            if current_elf_calories > biggest_three_elf_calories[0]:
                biggest_three_elf_calories.append(current_elf_calories)
                biggest_three_elf_calories.sort()
                biggest_three_elf_calories = biggest_three_elf_calories[1:4]
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

    return sum(biggest_three_elf_calories)


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
