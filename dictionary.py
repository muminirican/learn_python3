#!/usr/local/bin/python3
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5 }
x['one'] = 2342342
for i in x:
    print('i is {}'.format(i))
for k, v in x.items():
    print('key is {}, value is {}'.format(k, v))