#!/usr/bin/env python3

import platform

version = platform.python_version()
print('This is pyhton version {}'.format(version))

x= 7
print(f'x is {x}')
print(type(x))

y= 'seven'.upper()
print(f'y is {y}')
print(type(y))

z =[1, 2, 3, 4, 5]
print(type(z))
z[1] = 'mumin'

for i in z:
    print(f'i is {i}')

a =(1, 2, 3, 4, 5)
print(type(a))
#a[2] = 'mumin' tuples are immutable

for i in a:
    print(f'i is {i}')
###---------------------
print('-----------------------')
b =range(5, 10)
print(type(b))
#b[2] = 'mumin' ranges are immutable

for i in b:
    print(f'i is {i}')

print('-----------------------')
c =list(range(5, 10))
print(type(c))
c[2] = 'mumin'

for i in c:
    print(f'i is {i}')
