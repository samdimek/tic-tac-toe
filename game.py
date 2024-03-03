# tic-tac-toe game

import os
os.system("cls")

class Board():

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print("%s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print("%s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        print("%s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True

        # write logic for winning here!
        return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

board = Board()

def print_header():
    print("Welcome to Tic-Tac-Toe\n")


def refresh_screen():
    # clears screen
    os.system("cls")

    # print header
    print_header()

    # show board
    board.display()


while True:
    refresh_screen()

    # Get X input
    x_choice = int(input("\nX) Please choose 1 - 9. > "))

    # Update Board
    board.update_cell(x_choice, "X")

    # Refresh screen
    refresh_screen()

    # Check for an X win
    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Get O input
    o_choice = int(input("\nO) Please choose 1 - 9. > "))

    # Update Board
    board.update_cell(o_choice, "O")