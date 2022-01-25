# -*- coding: utf-8 -*-
import game


def main():
    while True:  # loop until user say no to replay
        game.start()
        winner = game.run()
        replay = input("\nVoulez vous rejouer ? (Y/n) ")
        if replay != 'Y' and replay != 'y':
            exit()


if __name__ == '__main__':
    main()
