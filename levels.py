import numpy as np
from player import player
from enemy import enemy


def start():
    print('        _            _   _   _             ___  _         ')
    print('       | \\ | | |\\ | / _ |_  / \\ |\\ | |   |  |  |_          ')
    print('       |_/ |_| | \\| \\_/ |_  \\_/ | \\| |_  |  |  |_          \n')
    print('Controls')
    print('w - move up')
    print('a - move left')
    print('d - move right')
    print('s - move down')
    print('mouse click - fire projectile\n')
    print('Enter a number to choose a difficulty')
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    print('4. Expert\n')
    return input()

easy = [
[enemy(300, 300, 9)], 
[enemy(10, 300, 10), enemy(450, 450, 9)],
[enemy(450, 450, 10), enemy(150, 150, 10), enemy(150, 450, 10), enemy(450, 150, 10)],
[enemy(10, 110, 9), enemy(210, 310, 11), enemy(410, 510, 9), enemy(110, 510, 11)],
[enemy(200, 200, 10), enemy(450, 450, 10), enemy(150, 450, 10), enemy(450, 150, 10), enemy(150, 150, 10), enemy(400, 400, 10)],
[enemy(200, 400, 13), enemy(400, 200, 13)]
]

medium = [
[enemy(300, 300, 7), enemy(300, 300, 12)], 
[enemy(300, 300, 9), enemy(300, 300, 12), enemy(300, 300, 15)],
[enemy(300, 300, 8), enemy(300, 300, 9), enemy(300, 300, 13), enemy(300, 300, 13.5), enemy(300, 300, 14), enemy(300, 300, 14.5)],
[enemy(10, 300, 11), enemy(520, 300, 10), enemy(300, 10, 11), enemy(300, 520, 10), enemy(10, 300, 9), enemy(520, 300, 11), enemy(300, 300, 9)],
[enemy(520, 520, 14.5)],
[enemy(200, 400, 14), enemy(400, 200, 14)]
]

hard = [
[enemy(10, 30, 7), enemy(10, 520, 12), enemy(200, 30, 12), enemy(200, 520, 7), enemy(500, 30, 7), enemy(500, 520, 12), enemy(200, 200, 7), enemy(200, 400, 11), enemy(400, 200, 9), enemy(400, 400, 9)], 
[enemy(200, 200, 8), enemy(200, 400, 8), enemy(400, 400, 8), enemy(400, 200, 8), enemy(100, 100, 10), enemy(500, 500, 10), enemy(500, 100, 10), enemy(100, 500, 10)],
[enemy(10, 30, 12), enemy(10, 520, 7), enemy(200, 30, 7), enemy(200, 520, 12), enemy(500, 30, 7), enemy(500, 520, 12), enemy(200, 200, 11), enemy(200, 400, 9), enemy(400, 200, 7), enemy(400, 400, 9)],
[enemy(300, 300, 14), enemy(500, 500, 14), enemy(100, 100, 14), enemy(100, 300, 10), enemy(300, 500, 10), enemy(300, 100, 10), enemy(500, 300, 10)],
[enemy(10, 30, 9), enemy(10, 520, 12), enemy(200, 30, 7), enemy(200, 520, 12), enemy(500, 30, 7), enemy(500, 520, 7), enemy(200, 200, 12), enemy(200, 400, 9), enemy(400, 200, 11), enemy(400, 400, 7)],
[enemy(30, 10, 10), enemy(520, 10, 15), enemy(30, 200, 15), enemy(400, 400, 10), enemy(30, 500, 10), enemy(520, 500, 15), enemy(200, 200, 10), enemy(500, 200, 14), enemy(300, 200, 12), enemy(200, 400, 12)]
]

expert = [
[enemy(10, 30, 8), enemy(10, 520, 13), enemy(200, 30, 12), enemy(200, 520, 7), enemy(500, 30, 8), enemy(500, 520, 13), enemy(200, 200, 7), enemy(200, 400, 11), enemy(400, 200, 9), enemy(400, 400, 9)], 
[enemy(300, 300, 14), enemy(500, 500, 14), enemy(100, 100, 14), enemy(100, 300, 10), enemy(300, 500, 10), enemy(300, 100, 10), enemy(500, 300, 10), enemy(500, 100, 10), enemy(100, 500, 10)],
[enemy(10, 30, 12), enemy(10, 520, 8), enemy(200, 30, 7), enemy(200, 520, 13), enemy(500, 30, 7), enemy(500, 520, 13), enemy(200, 200, 12), enemy(200, 400, 9), enemy(400, 200, 7), enemy(400, 400, 9)],
[enemy(300, 300, 14), enemy(500, 500, 14), enemy(100, 100, 14), enemy(100, 300, 10), enemy(300, 500, 10), enemy(300, 100, 10), enemy(500, 300, 10), enemy(500, 100, 10), enemy(100, 500, 10), enemy(700, 700, 17)],
[enemy(10, 30, 9), enemy(10, 520, 12), enemy(200, 30, 7), enemy(200, 520, 12), enemy(500, 30, 7), enemy(500, 520, 7), enemy(-30, -30, 12), enemy(-30, 630, 11), enemy(400, 200, 9), enemy(400, 400, 7)],
[enemy(10, 300, 10), enemy(520, 300, 15), enemy(50, 200, 15), enemy(480, 200, 10), enemy(200, 100, 10), enemy(300, 100, 15), enemy(50, 400, 10), enemy(480, 400, 14), enemy(200, 500, 12), enemy(300, 500, 12)]
]
