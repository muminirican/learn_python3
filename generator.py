#!/usr/bin/env python3

def main():
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    print(type(args))
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError(f'expected at least one argument , got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()

def f1():
    print('this is f1')
   # print(type(print('test')))

f1()

def f3():
    def f4():
        print('this is f4')
    f4()
    return f4

y = f3()
print(type(y))
#f3()
#y()

def f10(f):
    print('f10 called')
    def f11():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f11

def f12():
    print('this is f 12')

f10(f12)

x = f10(f12)
x()

def f13():
    print('this is f13')

@f10 #decorator
def f14():
    print('this is f14')

f10(f14)

#z = f10(f13)()

f13 = f10(f13)
f13()

f14()

