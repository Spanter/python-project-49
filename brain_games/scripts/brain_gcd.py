#!/usr/bin/env python3
from brain_games.engine import get_start_game
from brain_games.games import gcd


def main():
    get_start_game(gcd)


if __name__ == '__main__':
    main()
