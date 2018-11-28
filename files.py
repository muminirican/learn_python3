#!/usr/local/bin/python3
import sys

def main():
    f = open('lines.txt')
    print(type(f))

    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()