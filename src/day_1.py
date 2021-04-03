def get_data():
    with open("../data/day_1_input.txt") as f:
        rows = f.readlines()
        return list(map(int, rows))


def main():
    print(get_data())


if __name__ == "__main__":
    main()
