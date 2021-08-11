#!/usr/bin/env python3

"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""


def main():
    """On this farm there was a..."""

    farms = [{"name": "NE Farm", agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
        {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for farm in farms:
    print(farm.get("name", "Unknown Farm"), end=":\n")

for agri in farm.get("agriculture"):
    print(" -", agri)

if __name__ == "__main__":
    main()
