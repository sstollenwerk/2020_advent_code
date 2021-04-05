from typing import Iterator

import more_itertools

def get_data() -> list[int]:
    with open("../data/d10.txt") as f:
        rows = f.readlines()
        return list(map(int, rows))


def use_all_order(vals:list[int]) -> list[int]:
    return sorted(vals)

def diffs(vals:list[int]) -> list[int]:
    return [b-a for (a,b) in more_itertools.pairwise(iter(vals))]

def main():
    vals = get_data() + [0] + [ max(get_data()) + 3]
    diff = diffs(use_all_order(vals))

    print(diff.count(1) * diff.count(3) )


if __name__ == "__main__":
    main()
