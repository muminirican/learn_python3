#!/usr/bin/env python3
def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    x = dict(param1 = 'param1', param2 = 'param2', param3 = 'param3')
    kitten(**x)
    y = {'param4' : 'param4', 'param5' : 'param5', 'param6' : 'param6'}
    kitten(**y)


def kitten(**kwargs):
    if len(kwargs):
        for s in kwargs:
            print('Kitten {} says {} '. format(s, kwargs[s]))
        else:
            print('loop ended')
    else:
        print('else')

if __name__ == '__main__': main()
