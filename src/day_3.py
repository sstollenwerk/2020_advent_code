#!/usr/bin/env python3.9


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


def find_hit(angle: int, rows: list[CircList[bool]], index: int = 0) -> int:
    if not rows:
        return 0
    x, *xs = rows
    return x[index] + find_hit(angle, xs, index + angle)


def main():
    vals = get_data()
    print(find_hit(3, vals))


if __name__ == "__main__":
    main()
