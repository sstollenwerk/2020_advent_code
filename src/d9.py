from typing import Iterator



def get_data() -> list[int]:
    with open("../data/d9.txt") as f:
        rows = f.readlines()
        return list(map(int, rows))

def invalids(vals:list[int], premb_len:int) -> Iterator[int]:
    for i in range(premb_len, len(vals)):
        check = vals[i]
        prevs = set(vals[i-premb_len:i] )

        valid = any((a for a in prevs
            if check - a in prevs))
        if not valid:
            yield check


def main():
    vals = get_data()
    print(next(invalids(vals, 25)))


if __name__ == "__main__":
    main()
