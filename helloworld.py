#!/usr/local/bin/python3

x = 42
print("Hello World {}".format(x))

y = 104
t = 'string value'


#deprecated way
print('hello %d' % y)

print('hello %s' % t)

#newer version for the format

print(f'hello with f {y}')