def read_batch(filename: str) -> list[list[str]]:
    with open("../data/" + filename) as f:
        groups = f.read().split("\n\n")
        return [g.split() for g in groups]
