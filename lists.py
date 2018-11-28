#!/usr/bin/env python3

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(type(game))
    game.append('Computer')
    game.insert(0,'Computer')
    print_list(game)
    i = game.index('Paper')
    print(game[i])
    y = game[1:3]
    print(id(y))
    print(type(y))
    print(y)

def print_list(o):
    for i in o: print(i, end =' ', flush=True)
    print()

if __name__ == '__main__': main()