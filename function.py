#!/usr/bin/env python3
def main():
    x = 5 #integers are immutable
    y = x
    print(id(x))
    print(id(y))
    #kitten(5)
    print(f'in main: x is {x}  ')
    dog('param1', 'param2')

def kitten(n):
    print(id(n))
    n = 3
    print('Meow.')
    print(n)
    print(id(n))

def dog(*args):
    if len(args):
        for s in args:
            print(s)
    else:
            print('Meow')



if __name__ == '__main__': main()
