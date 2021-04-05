import common

Bag = str

Contain = dict[Bag, int]

Tree = dict[Bag, Contain]


class TreeFunc:
    """
    for funcs where I'll be passing the tree around everywhere anyway
    especially recursive funcs
    """

    def __init__(self, tree: Tree):
        self.tree: Tree = tree

    def contain(self, bag: Bag) -> set[Bag]:
        """
        feels like bad O(n) but ran fast enough on supplied input
        """
        tree = self.tree
        outs = {b for b, cont in tree.items() if bag in cont.keys()}
        return outs.union(*map(self.contain, outs))


def get_data() -> list[str]:
    with open("../data/d7.txt") as f:
        rows = f.readlines()
        return list(rows)


# @common.out_data
def parse_row(val: str) -> Tree:
    val = (
        val.replace("bags", "bag")
        .replace("bag", "")
        .replace("no", "0")
        .replace(".", "")
    )
    out, within = val.split("contain")
    out = out.strip()
    cont = {}
    within = within.split(",")
    for data in within:
        amt, bag = data.split(maxsplit=1)
        bag = bag.strip()
        amt = int(amt)
        if amt:
            cont[bag] = amt

    return {out: cont}


def parse_all(vals: list[str]) -> Tree:
    tree = {key: val for d in map(parse_row, vals) for key, val in d.items()}
    return tree


def main():
    vals = get_data()
    tree = parse_all(vals)
    res = TreeFunc(tree).contain("shiny gold")
    # print(res)
    print(len(res))


if __name__ == "__main__":
    main()
