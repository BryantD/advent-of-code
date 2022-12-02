#!/usr/bin/env python3


def rps1(strat):
    # stupid clunky but fast
    match strat:
        case "A X":
            score = 3
        case "A Y":
            score = 6
        case "A Z":
            score = 0
        case "B X":
            score = 0
        case "B Y":
            score = 3
        case "B Z":
            score = 6
        case "C X":
            score = 6
        case "C Y":
            score = 0
        case "C Z":
            score = 3

    match strat[-1]:
        case "X":
            score += 1
        case "Y":
            score += 2
        case "Z":
            score += 3

    return score


def rps2(strat):
    rps = "ABC"
    match strat[-1]:
        case "X":
            score = 0
            choice_score = (rps.index(strat[0]) + 1) - 1
            if choice_score == 0:
                choice_score = 3
        case "Y":
            score = 3
            choice_score = rps.index(strat[0]) + 1
        case "Z":
            score = 6
            choice_score = (rps.index(strat[0]) + 1) + 1
            if choice_score == 4:
                choice_score = 1

    score += choice_score
    
    return score


def part1(data):
    total_score = 0
    for match in data:
        total_score += rps1(match)

    return total_score


def part2(data):
    total_score = 0
    for match in data:
        total_score += rps2(match)

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
