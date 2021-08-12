#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and 
performing HTTP look-ups with the python standard library."""

import re
import urllib.request

def main():
    """Search a website's content"""

    print("Where should we search?")
    url = input("> ")

    print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
    searchFor = input("> ")

    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    if re.search(searchFor, searchMe):
        print("Found a  match!")
    else:
        print("No match!")

if __name__ == "__main__":
    main()
