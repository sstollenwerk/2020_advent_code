#!/usr/bin/env python3.9

import math


def get_data() -> list[int]:
    with open("../data/day_1_input.txt") as f:
        rows = f.readlines()
        return list(map(int, rows))


def find_sum(total: int, nums: set[int]) -> tuple[int, int]:
    for i in nums:
        if (j := (total - i)) in nums:
            return (i, j)
    raise ValueError


def find_sum_n(n: int, total: int, nums: set[int]) -> list[int]:
    assert n > 0
    if n == 1:
        if total not in nums:
            raise ValueError
        else:
            return [total]
    for i in nums:
        try:
            return [i] + find_sum_n(n - 1, total - i, nums - {total})
        except ValueError:
            pass
    raise ValueError


def main():
    vals = set(get_data())
    x, y = find_sum(2020, vals)
    assert sorted(find_sum(2020, vals)) == sorted(find_sum_n(2, 2020, vals))
    print(x * y)
    print(math.prod(find_sum_n(3, 2020, vals)))


if __name__ == "__main__":
    main()
