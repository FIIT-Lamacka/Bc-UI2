from UI_class import *


def start5():

    five_list = []
    first = Board(5)
    first.create_start_point()
    five_list.append(first)

    for i in range(4):
        new = Board(5)
        new.create_start_random()
        five_list.append(new)

    for board in five_list:
        board.print_board()
        board.cull_moves()
        board.print_moves()
