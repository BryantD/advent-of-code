#!/usr/bin/env python3


def main():

    marker = []
    solution1 = 0
    with open("data.txt") as data_file:
        while True:
            c = data_file.read(1)
            if c:
                solution1 += 1
                if len(marker) < 4:
                    marker.append(c)
                else:
                    marker.pop(0)
                    marker.append(c)
                if len(set(marker)) == 4:
                    break

    print(marker)
    print(solution1)

    marker = []
    solution2 = 0
    with open("data.txt") as data_file:
        while True:
            c = data_file.read(1)
            if c:
                solution2 += 1
                if len(marker) < 14:
                    marker.append(c)
                else:
                    marker.pop(0)
                    marker.append(c)
                if len(set(marker)) == 14:
                    break

    print()

    print(marker)
    print(solution2)


if __name__ == "__main__":
    main()
