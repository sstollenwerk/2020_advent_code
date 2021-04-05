#!/usr/bin/env python3.9
from enum import Enum, auto

import common


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Operation(AutoName):
    nop = auto()
    acc = auto()
    jmp = auto()


Instruction = tuple[Operation, int]


def parse(row: str) -> Instruction:
    op, n = row.split()

    op = next((o for o in Operation if o.value == op))

    return (op, int(n))


def emulate(code: list[Instruction]) -> int:
    seen = set()
    accumulator = 0

    instruc = 0
    while True:
        if instruc in seen:
            raise ValueError
        seen.add(instruc)
        if instruc >= len(code):
            break
        command, amt = code[instruc]

        if command == Operation.jmp:
            instruc += amt
            continue
        elif command == Operation.acc:
            accumulator += amt
        else:
            pass
        instruc += 1
    return accumulator


def try_ops(code: list[Instruction]) -> int:
    for i, el in enumerate(code):
        revs = {Operation.nop, Operation.jmp}
        if el[0] in revs:
            new_el = (list(revs - {el[0]})[0], el[1])

            poss = code.copy()
            poss[i] = new_el
            try:

                return emulate(poss)
            except ValueError as e:
                pass


def main():
    vals = list(map(parse, common.read_lines("d8.txt")))
    print(try_ops(vals))


if __name__ == "__main__":
    main()
