#!/usr/bin/env python3.9
from typing import TypeVar, Callable
from collections import defaultdict

T = TypeVar("T")
V = TypeVar("V")

Ticket = tuple[int, int]


def groupby(vals: list[T], key: Callable[[T], V]) -> dict[V, list[T]]:
    groups = defaultdict(list)
    for v in vals:
        groups[key(v)].append(v)
    return dict(groups)


def get_data() -> list[str]:
    with open("../data/d5.txt") as f:
        rows = f.readlines()
        return list(rows)


def split_list(vals: list[T]) -> tuple[list[T], list[T]]:
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


def find_missing(tickets: list[Ticket]) -> Ticket:
    groups_ = groupby(tickets, lambda x: x[0])
    groups = {k: {i[1] for i in v} for k, v in groups_.items()}

    expected = set(range(8))
    for row, seats in groups.items():
        for seat in (missing := expected - seats) :
            if seat in groups[row - 1] and seat in groups[row + 1]:
                return (row, seat)

    raise ValueError


def main():
    vals = map(find_pos, get_data())
    print(seat_id(find_missing(list(vals))))


if __name__ == "__main__":
    main()
