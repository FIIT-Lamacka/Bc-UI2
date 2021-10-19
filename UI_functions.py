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

    #for board in five_list:
       # solve(board)

    solve(five_list[0])


def solve(board):
    try:
        while not board.check_fullness():
            #board.print_moves()
            while len(board.unused_moves) == 0:
                board = board.parent
            board = board.create_child()
        board.print_board()
    except AttributeError:
        print(Back.RED + "NEPODARILO SA NAJSŤ RIEŠENIE" + Style.RESET_ALL)



