#!/usr/bin/env python3.9

from functools import partial
import math


class CircList(list):
    def __getitem__(self, i):
        index = i % len(self)

        return list(self)[index]


def parse_row(row: str) -> CircList[bool]:
    row = row.strip()
    if not (set(row) <= {"#", "."}):
        raise ValueError
    return CircList([c == "#" for c in row])


def get_data() -> list[CircList[bool]]:
    with open("../data/day_3_input.txt") as f:
        rows = f.readlines()
        return list(map(parse_row, rows))


def find_hit(rows: list[CircList[bool]], right: int, down: int, index: int = 0) -> int:
    if not rows:
        return 0

    rows[0][index]
    return rows[0][index] + find_hit(rows[down:], right, down, index + right)


def main():
    vals = get_data()
    hit = partial(find_hit, vals)
    angles = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(math.prod(hit(*ang) for ang in angles))


if __name__ == "__main__":
    main()
