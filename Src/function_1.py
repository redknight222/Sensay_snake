import random
import keyboard

initial_size = []
board_size = 10
stop_vector = [1, 10]


def hello():
    print('Hello this is snake')
    return input('Do you want to start a game?\n(press Yes/No)') == 'Yes'


def snake():  # create initial snake size
    global initial_size
    initial_size = [[board_size // 2, board_size // 2], [board_size // 2, board_size // 2 - 1]]
    print(initial_size)


def down_move():  # change direction
    while True:
        for i in range(1, len(initial_size)):
            initial_size[i][0] = initial_size[i - 1][0]
            initial_size[i][1] = initial_size[i - 1][1]
        initial_size[0][0] -= 1
        if stop_game():
            continue
        else:
            break


def up_move():  # change direction
    while True:
        for i in range(1, len(initial_size)):
            initial_size[i][0] = initial_size[i - 1][0]
            initial_size[i][1] = initial_size[i - 1][1]
        initial_size[0][0] += 1
        if stop_game():
            continue
        else:
            break


def left_move():  # change direction
    while True:
        for i in range(1, len(initial_size)):
            initial_size[i][0] = initial_size[i - 1][0]
            initial_size[i][1] = initial_size[i - 1][1]
        initial_size[0][1] -= 1
        if stop_game():
            continue
        else:
            break


def right_move():  # change direction
    while True:
        for i in range(1, len(initial_size)):
            initial_size[i][0] = initial_size[i - 1][0]
            initial_size[i][1] = initial_size[i - 1][1]
        initial_size[0][1] += 1
        if stop_game():
            continue
        else:
            break


def stop_game():  # check parameters of stopping game
    for i in initial_size[0]:
        if i[0] in stop_vector or i[1] in stop_vector:
            print('Game over')
            return False
        elif i in initial_size[1:]:
            print('Game over')
            return False
        else:
            return True


def apple_show():  # create apple place
    while True:
        apple_place = [random.randint(1, 9), random.randint(1, 9)]
        if apple_place[0] in stop_vector or apple_place[1] in stop_vector:
            continue
        elif apple_place in initial_size:
            continue
        else:
            break




def print_board():  # print snake, apple and board to screen
    board_array = [['' for _ in range(board_size)] for _ in range(board_size)]
    for i in range(board_size):
        print(board_array[i])


snake()
down_move()
print(initial_size)
