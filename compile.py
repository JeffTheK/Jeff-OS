#!/usr/bin/env python3

from os import system

def main():
    print("[OK]compiling")
    system("gcc src/bin/python.c -o src/bin/python")

if __name__ == "__main__":
    main()