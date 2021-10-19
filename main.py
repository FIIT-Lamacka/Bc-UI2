from UI_functions import *

if __name__ == '__main__':
    #start5()


    first = Board(5)
    first.create_start_random()
    first.cull_moves()
    solve(first)