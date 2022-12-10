#!/usr/bin/env python3

def move_tail(head, tail):
    if head != tail:
        if abs(head[1] - tail[1]) > 1 or abs(head[0] - tail[0]) > 1:
            if tail[0] == head[0]:      # they're on the same X axis
                if tail[1] > head[1]:
                    tail[1] -= 1
                else:
                    tail[1] += 1
            elif tail[1] == head[1]:    # they're on the same Y axis
                if tail[0] > head[0]:
                    tail[0] -= 1
                else:
                    tail[0] += 1
            else:                       # diagonal!
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1
                if head[1] >= tail[1]:
                    tail[1] += 1
                else:
                    tail[1] -= 1
    
    return tail

def part1(data):
    h = [0, 0]
    t = [0, 0]
    
    tail_visits = set()
    tail_visits.add(",".join(map(str, t)))
    
    for line in data:
        (direction, count) = line.split()
        count = int(count)
        while count:
            match direction:
                case "U":
                    h[1] += 1
                case "D":
                    h[1] -= 1
                case "R":
                    h[0] += 1
                case "L":
                    h[0] -= 1
                    
#             print(f"{line} moves H to [{h[0]}, {h[1]}]")

            t = move_tail(h, t)
            count -= 1
            tail_visits.add(",".join(map(str, t)))

    return len(tail_visits)


def part2(data):
    rope = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
    ]
    
    tail_visits = set()
    tail_visits.add(",".join(map(str, rope[9])))
    
    for line in data:
        (direction, count) = line.split()
        count = int(count)
        while count:
            match direction:
                case "U":
                    rope[0][1] += 1
                case "D":
                    rope[0][1] -= 1
                case "R":
                    rope[0][0] += 1
                case "L":
                    rope[0][0] -= 1

            for i in range(1, len(rope)):
                rope[i] = move_tail(rope[i-1], rope[i])
            count -= 1
            tail_visits.add(",".join(map(str, rope[9])))

    return len(tail_visits)


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
