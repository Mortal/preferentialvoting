import argparse
import collections


parser = argparse.ArgumentParser()
parser.add_argument("filename")


def main() -> None:
    args = parser.parse_args()
    with open(args.filename) as fp:
        lines = [l.strip() for l in fp]
    optionss = {frozenset(line) for line in lines}
    assert len(optionss) == 1, optionss
    options_set, = optionss
    options = sorted(options_set)
    removed = set[str]()
    while len(removed) + 1 < len(options):
        topvotes = [next(c for c in line if c not in removed) for line in lines]
        print("Current options in this round:", sorted(set(options) - removed))
        counts = collections.Counter(topvotes)
        print("Count of votes in this round:", counts)
        mincount = min(counts.values())
        maxcount = max(counts.values())
        if mincount == maxcount:
            print("Stemmelighed")
            break
        r = {c for c in counts if counts[c] == mincount}
        print(f"Eliminating option(s) with {mincount} votes: {sorted(r)}")
        removed |= r
        print("")
    print("The winner is", set(options) - removed)


if __name__ == "__main__":
    main()
