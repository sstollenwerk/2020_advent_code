from dataclasses import dataclass
from typing import Optional

@dataclass
class Passport:
    byr:str
    iyr:str
    eyr:str
    hgt:str
    hcl:str
    ecl:str
    pid:str
    cid:Optional[str] = None

    def __post_init__(self):
        hts = {'cm':(150,193), 'in':(59,76)}
        height, meas = int(self.hgt[:-2]), self.hgt[-2:]
        ht_rng = hts[meas]

        reqs = [
        1920 <= int(self.byr) <= 2002,
        2010 <= int(self.iyr) <= 2020,
        2020 <= int(self.eyr) <= 2030,
        ht_rng[0] <= height <= ht_rng[1],
        self.hcl[0] == "#" and isinstance(  int(self.hcl[1:], 16), int) and len(self.hcl) == 7,
        # second cond checking if it parses
        self.ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        len(self.pid) == 9 and isinstance( int(self.pid), int),

        ]
        if not all(reqs): raise TypeError


def get_data() -> list[str]:
    with open("../data/day_4_input.txt") as f:
        groups = f.read().split('\n\n')
        return list(groups)

def parse(val:str) -> Passport:
    data = {}
    groups = val.split()
    for g in groups:
        k, v = g.split(':')
        data[k] = v

    return Passport(**data)

def valid(group:str) -> bool:
    try:
        parse(group)
    except (TypeError, KeyError, ValueError) as e:
        return False
    else:
        return True



def main():
    vals = get_data()
    print(len(list(filter(valid, vals))))


if __name__ == "__main__":
    main()
