#############################################################
# file : board.py
# WRITER : DANIEL , danieltal ,204501712
# EXERCISE : ex9
#############################################################
EMPTY = "_"
from car import *

class Board:
    """This class creates a game board with vehicles"""

    def __init__(self):
        self.__board_game = [["_" for i in range(7)] for j in range(7)]
        self.__board_game[3].append('EXIT')
        self.__cars_lst = []

    def __str__(self):
        print_board = ("* " * 9) + "\n"
        for i in range(len(self.__board_game)):
            print_board += "* "
            for j in range(len(self.__board_game[i])):
                print_board += self.__board_game[i][j] + " "
            if i != 3:
                print_board += "*"
            print_board += "\n"
        print_board += ("* " * 9)
        return str(print_board)

    def cell_list(self):

        cell_list = [(i, j) for i in range(len(self.__board_game)) for j in
                     range(len(self.__board_game[i]))]
        return cell_list

   # def possible_moves1(self):
#
 #       dic_direct = {"u": "up", "d": "down", "r": "right", "l": "left"}
  #      list_option_move = []
   #     for i in self.__cars_lst:
    #        posible_move = i.possible_moves()
     #       for j in posible_move:
      #          move = i.movement_requirements(j)[0]
       #         if move in self.cell_list() and self.cell_content(
        #                move) is None:
         #           list_option_move.append(
          #              (i.get_name(), j, "you can move " + dic_direct[j]))
       # return list_option_move

    def possible_moves(self):
        list_option_move = []
        for car in self.__cars_lst:
            dict_car=car.possible_moves()
            #print(dict_car)
            car_key=list(dict_car.keys())
           # print(car_key)
            list_option_move.append((car.get_name(),car_key[0],dict_car[car_key[0]]))
            list_option_move.append(
                (car.get_name(), car_key[1], dict_car[car_key[1]]))

        return list_option_move







    def target_location(self):
        return (3, 7)

    def cell_content(self, coordinate):
        if self.__board_game[coordinate[0]][coordinate[1]] == EMPTY or \
                self.__board_game[coordinate[0]][coordinate[1]] == "EXIT":
            return None
        else:
            return self.__board_game[coordinate[0]][coordinate[1]]


    def add_car(self, car):
        car_name = car.get_name()
        car_coord = car.car_coordinates()
        len(car_coord)
        board_coord = self.cell_list()
        for i in car_coord:
            if i not in board_coord:
                return False
            if self.cell_content(i) != None:
                return False
        for i in car_coord:
            self.__board_game[i[0]][i[1]] = car_name
        self.__cars_lst.append(car)
        return True





    def move_car(self, name, movekey):
        for i in self.__cars_lst:
            if i.get_name() == name:
                for j in self.possible_moves():
                    if j[0] == name and j[1] == movekey:
                        car_coord = i.car_coordinates()
                        length_car = len(car_coord)

                        if movekey == "u" or movekey == "l":
                            last_cord = car_coord[length_car - 1:]
                            self.__board_game[last_cord[0][0]][
                                last_cord[0][1]] = EMPTY
                            i.move(movekey)
                            new_cord = i.car_coordinates()[0]
                            self.__board_game[new_cord[0]][new_cord[1]] = name

                        elif movekey == "d" or movekey == "r":
                            self.__board_game[car_coord[0][0]][
                                car_coord[0][1]] = EMPTY
                            i.move(movekey)
                            last_cord = i.car_coordinates()[length_car - 1:]
                            self.__board_game[last_cord[0][0]][
                                last_cord[0][1]] = name

                        return True
        return False
