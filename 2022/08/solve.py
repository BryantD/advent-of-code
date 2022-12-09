#!/usr/bin/env python3


def trace_count(data, i, j, xdir, ydir):
    visible = True
    height = int(data[i][j])
    x = i
    y = j
    count = 0
    while (
        x > 0 and y > 0 and x < len(data[i]) - xdir and y < len(data) - ydir and visible
    ):
        x += xdir
        y += ydir

        if int(data[x][y]) > height:
            visible = False
        else:
            count += 1
            if int(data[x][y]) == height:
                visible = False

    return count


def trace(data, i, j, xdir, ydir):
    visible = True
    height = int(data[i][j])
    x = i
    y = j
    while (
        x > 0 and y > 0 and x < len(data[i]) - xdir and y < len(data) - ydir and visible
    ):
        x += xdir
        y += ydir

        if int(data[x][y]) >= height:
            visible = False

    return visible


def part1(data):
    total_score = 0
    i = 0
    for line in data:
        j = 0
        for char in line:
            if (
                trace(data, i, j, 1, 0)
                or trace(data, i, j, -1, 0)
                or trace(data, i, j, 0, 1)
                or trace(data, i, j, 0, -1)
            ):
                total_score += 1

            j += 1
        i += 1

    return total_score


def part2(data):
    high_score = 0
    i = 0
    for line in data:
        j = 0
        for char in line:
            scenic_score = (
                trace_count(data, i, j, 1, 0) *
                trace_count(data, i, j, -1, 0) *
                trace_count(data, i, j, 0, 1) *
                trace_count(data, i, j, 0, -1)
            )
            high_score = max(scenic_score, high_score)

            j += 1
        i += 1

    return high_score


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
