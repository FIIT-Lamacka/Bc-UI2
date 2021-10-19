import copy
import random
from tabulate import *
from colorama import *

init()


class Move:
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

# PyCharm vyhadzuje chybný warning, treba ho ignorovať
# noinspection PyTypeChecker


class Board:
    def __init__(self, size):

        self.gen = 1
        self.size = size
        self.board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            self.board.append(row)

        self.parent = None
        self.children = []
        self.position = None
        self.unused_moves = [Move(2, 1),  Move(-2, 1),  Move(1, 2),   Move(-1, 2),
                             Move(2, -1), Move(-2, -1), Move(1, -2), Move(-1, -2)]

    def check_fullness(self):
        if any(0 in row for row in self.board):
            return False
        else:
            return True

    def print_board(self):

        dummy_board = copy.deepcopy(self.board)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    dummy_board[i][j] = Fore.RED + str(self.board[i][j]) + Style.RESET_ALL
                else:
                    dummy_board[i][j] = Fore.GREEN + str(self.board[i][j]) + Style.RESET_ALL

        print(tabulate(dummy_board, tablefmt="fancy_grid", stralign="center"))

    def create_start_point(self):
        self.board[self.size-1][0] = 1
        self.position = [self.size-1, 0]

    def create_start_random(self):
        r_vert = random.randint(0, self.size-1)
        r_hor = random.randint(0, self.size-1)

        self.board[r_vert][r_hor] = 1
        self.position = [r_vert, r_hor]

    def create_child(self):
        child = Board(self.size)
        child.parent = self
        child.board = copy.deepcopy(self.board)
        next_move = self.unused_moves.pop()

        child.position = [self.position[0] + next_move.vertical, self.position[1] + next_move.horizontal]
        child.gen = self.gen + 1
        child.board[child.position[0]][child.position[1]] = child.gen
        child.cull_moves()
        return child



    def cull_moves(self):
        unwanted = []
        for move in self.unused_moves:
            next_vert = self.position[0] + move.vertical
            next_horiz = self.position[1] + move.horizontal
            if next_vert >= self.size or next_vert < 0 or next_horiz >= self.size or next_horiz < 0:
                unwanted.append(move)
            elif self.board[next_vert][next_horiz] != 0:
                unwanted.append(move)

        for wrong in unwanted:
            self.unused_moves.remove(wrong)


    def print_moves(self):
        print("Available moves: " + str(len(self.unused_moves)))
        for moves in self.unused_moves:
            print("(" + str(moves.vertical) + ";" + str(moves.horizontal) + ")", end=" ")
        print("")
        new_board = copy.deepcopy(self)

        for moves in self.unused_moves:
            i = self.position[0] + moves.vertical
            j = self.position[1] + moves.horizontal
            new_board.board[i][j] = "X"

        for i in range(new_board.size):
            for j in range(new_board.size):
                if new_board.board[i][j] != 0 and new_board.board[i][j] != "X":
                    new_board.board[i][j] = Fore.GREEN + str(new_board.board[i][j]) + Style.RESET_ALL
                elif i == self.position[0] and j==self.position[1]:
                    new_board.board[i][j] = Back.BLUE + Fore.BLACK + str(new_board.board[i][j]) + Style.RESET_ALL
                elif new_board.board[i][j] == "X":
                    new_board.board[i][j] = Back.YELLOW + Fore.BLACK + "X" + Style.RESET_ALL
                else:
                    new_board.board[i][j] = Fore.RED + str(new_board.board[i][j]) + Style.RESET_ALL

        print(tabulate(new_board.board, tablefmt="fancy_grid", stralign="center"))
