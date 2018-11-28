#!/usr/local/bin/python3


import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line 2')
    if True:
        print('line 3')
    else:
        print('not true')

if __name__ == '__main__': main()