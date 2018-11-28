#!/usr/bin/env python3

def main():
    seq = range(11)
    print(type(seq))
    print_seq(seq)
    print_seq([x * 2 for x in seq])
    print_seq([x for x in seq if x % 3 !=0])
    print_seq([(x, x**2) for x in seq])
def print_seq(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()