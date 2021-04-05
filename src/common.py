def read_batch(filename: str) -> list[list[str]]:
    with open("../data/" + filename) as f:
        groups = f.read().split("\n\n")
        return [g.split() for g in groups]


def read_lines(filename: str) -> list[str]:
    with open("../data/" + filename) as f:
        rows = f.readlines()
        return list(rows)


def out_data(f):
    def inner(*args, **kwargs):
        val = f(*args, **kwargs)
        print(val)
        return val

    return inner
