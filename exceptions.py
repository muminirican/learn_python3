#!/usr/local/bin/python3
import sys

def main():
    try:
        x = 5**2
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('don\' t divide by zero')
    except:
        print(f'unknown error: {sys.exc_info()}')
    else:
        print('good job')
        print(x)

if __name__ == '__main__': main()