#!/usr/bin/env python3.9
from typing import TypeVar

T = TypeVar("T")

Ticket = tuple[int, int]


def get_data() -> list[int]:
    with open("../data/d5.txt") as f:
        rows = f.readlines()
        return list(rows)


def split_list(vals: list[T]) -> list[T]:
    half = len(vals) // 2
    return vals[:half], vals[half:]


def sing_pos(part_ticket: str) -> int:
    """
    inefficient but n is small
    """
    alls = list(range(2 ** len(part_ticket)))
    ind = {"F": 0, "B": 1, "L": 0, "R": 1}
    for i in part_ticket:
        groups = split_list(alls)
        alls = groups[ind[i]]
    assert len(alls) == 1
    return alls[0]


def find_pos(ticket: str) -> Ticket:
    ticket = ticket.strip()
    row = ticket[:7]
    col = ticket[7:]
    return (sing_pos(row), sing_pos(col))


def seat_id(ticket: Ticket) -> int:
    a, b = ticket
    return 8 * a + b


def main():
    vals = get_data()
    print(max(map(seat_id, (map(find_pos, vals)))))


if __name__ == "__main__":
    main()
