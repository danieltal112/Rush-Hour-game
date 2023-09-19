#############################################################
# file : game.py
# WRITER : DANIEL , danieltal ,204501712
# EXERCISE : ex9
#############################################################

LIST_CARS = ["Y", "B", "O", "G", "W", "R"]


class Game:
    """
This class is a main class which runs the game and the other classes    """

    def __init__(self, board):
        self.__board = board

    def __single_turn(self):
        direction = ["u", "d", "r", "l"]
        print(self.__board)
        user_input = input("please enter color of car and direction to move.\n"
                           " e.g. for move red car left: R,l .\n"
                           "color car: what you see on the bord.\n"
                           "direction: u-up,d-down,l-left,r-right.\n"
                           "for exit from the game, enter  '!'  \n"
                           "Write here: ")
        if user_input == "!":
            return True
        if len(user_input) != 3 or user_input[1] != "," or user_input[
            0] not in LIST_CARS or user_input[2] not in direction:
            print("input not valid")
            return False
        if self.__board.move_car(user_input[0], user_input[2]):
            pass
        else:
            print("input not valid")
            return False

    def play(self):
        while self.__board.cell_content(
                self.__board.target_location()) is None:
            if self.__single_turn():
                print("game finish")
                return
        print(self.__board)
        print("WINNER")
        return


if __name__ == "__main__":
    import board
    from car import *
    import json
    import helper
    import sys

    board = board.Board()
    cars = helper.load_json(sys.argv[1])
    for name_car, data in cars.items():
        if len(data) == 3 and len(data[1]) == 2 and name_car in LIST_CARS and \
                data[0] < 5 and data[0] > 1 and (
                data[2] == 1 or data[2] == 0):
            car = Car(name_car, data[0], (data[1][0], data[1][1]), data[2])
            board.add_car(car)
    print(board.possible_moves())
    game = Game(board)
    game.play()
