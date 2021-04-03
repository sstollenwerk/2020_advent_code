#!/usr/bin/env python3.9

from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class PassRow:
    letter: str
    positions: tuple[int, int]
    password: str

    @cached_property
    def valid(self) -> bool:
        matches = [self.password[i] == self.letter for i in self.positions]
        return sum(matches) == 1


def get_data() -> list[str]:
    with open("../data/day_2_input.txt") as f:
        rows = f.readlines()
        return list(rows)


def parse_row(row: str) -> PassRow:
    info, password = row.split(":")
    password = password.strip()
    range_, letter = info.split()
    a, b = map(int, range_.split("-"))
    return PassRow(letter, (a - 1, b - 1), password)


def main():
    rows = map(parse_row, get_data())
    print(len([i for i in rows if i.valid]))


if __name__ == "__main__":
    main()
