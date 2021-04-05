#!/usr/bin/env python3.9

import common


def num_answers(vals: list[str]) -> int:
    return len(set().union(*map(set, vals)))


def main():
    groups = common.read_batch("d6.txt")
    # groups = common.read_batch("basic.txt")
    print(sum(map(num_answers, groups)))


if __name__ == "__main__":
    main()
