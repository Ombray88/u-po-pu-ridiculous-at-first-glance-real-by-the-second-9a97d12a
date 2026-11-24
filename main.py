#!/usr/bin/env python3
"""
Startup pitch generator: leasing angry guard geese to suburban homeowners
to scare off solar salesmen, billed as a monthly pest-control subscription.
"""
import os

def main():
    sentence = "We lease angry guard geese to suburban homeowners to terrorize door-to-door solar salesmen, billing households a monthly pest-control subscription."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)

if __name__ == "__main__":
    main()
