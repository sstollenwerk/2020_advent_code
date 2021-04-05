from typing import Iterator


def get_data() -> list[int]:
    with open("../data/d9.txt") as f:
        rows = f.readlines()
        return list(map(int, rows))


def invalids(vals: list[int], premb_len: int) -> Iterator[int]:
    for i in range(premb_len, len(vals)):
        check = vals[i]
        prevs = set(vals[i - premb_len : i])

        valid = any((a for a in prevs if check - a in prevs))
        if not valid:
            yield check


def range_sum(vals: list[int], find: int) -> list[int]:
    """
    leery about runtime inefficiency but ran nigh-instantaneously on supplied input
    """
    if min(vals) < 0:
        raise ValueError
    for i, el in enumerate(vals):
        poss = [el]
        for el2 in vals[i + 1 :]:
            poss.append(el2)
            if sum(poss) >= find:
                break
        if sum(poss) == find:
            return poss


def main():
    vals = get_data()
    find = next(invalids(vals, 25))

    nums = range_sum(vals, find)
    print(min(nums) + max(nums))


if __name__ == "__main__":
    main()
