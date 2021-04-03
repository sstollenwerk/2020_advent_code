def get_data() -> list[int]:
    with open("../data/day_1_input.txt") as f:
        rows = f.readlines()
        return list(map(int, rows))


def find_sum(total: int, nums: set[int]) -> tuple[int, int]:
    for i in nums:
        if (j := (total - i)) in nums:
            return (i, j)
    raise ValueError


def main():
    vals = set(get_data())
    x, y = find_sum(2020, vals)
    print(x * y)


if __name__ == "__main__":
    main()
