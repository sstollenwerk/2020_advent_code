from typing import Iterator

import more_itertools

from functools import cache


def get_data() -> list[int]:
    with open("../data/d10.txt") as f:
        rows = f.readlines()
        return list(map(int, rows))


@cache
def arrangements(vals: frozenset[int], n: int = None) -> int:
    if n is None:
        n = max(vals)
    if n == 0:
        return 1

    nexts = set(range(n - 3, n)) & vals

    return sum((arrangements(vals, i) for i in nexts))


def use_all_order(vals: list[int]) -> list[int]:
    return sorted(vals)


def diffs(vals: list[int]) -> list[int]:
    return [b - a for (a, b) in more_itertools.pairwise(iter(vals))]


def main():
    vals = get_data() + [0] + [max(get_data()) + 3]
    diff = diffs(use_all_order(vals))

    print(arrangements(frozenset(vals)))


if __name__ == "__main__":
    main()
