#!/usr/bin/env python3
words =['one', 'two', 'three', 'four', 'five']

n = 0
while(n < 5):
    print(words[n], end = ' ')
    n += 1

# fibonacci
a, b = 0, 1

while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

for i in words:
    print(i)


#definition of a function
def function(n):
    print(n)

function(2)

x = function(2)

#this will print none, like the any of scala
print(x)

def function2( n = 1):
    print(n)
    return n * 2
#call the cunction and assign the return value to y
y = function2()

print(y)

#or

print(function2(4))


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

n = 11
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')

def list_primes():
    for x in range(100):
        if isprime(x):
            print(x, end = ' ', flush = True)

list_primes()