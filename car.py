#############################################################
# file : car.py
# WRITER : DANIEL , danieltal ,204501712
# EXERCISE : ex9
#############################################################

class Car:
    """
    This class creates vehicles so that each vehicle has its own features
    """

    def __init__(self, name, length, location, orientation):
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        car_coordinates = []
        if self.__orientation == 0:
            for i in range(self.__length):
                car_coordinates.append(
                    (self.__location[0] + i, self.__location[1]))

        if self.__orientation == 1:
            for i in range(self.__length):
                car_coordinates.append(
                    (self.__location[0], self.__location[1] + i))
        return car_coordinates

    def possible_moves(self):
        dic_posible_move = {}
        if self.__orientation == 0:
            dic_posible_move['u'] = "cars move up"
            dic_posible_move['d'] = "cars move down"
        if self.__orientation == 1:
            dic_posible_move['r'] = "cars move right"
            dic_posible_move['l'] = "cars move left"
        return dic_posible_move

    def movement_requirements(self, movekey):
        if movekey not in self.possible_moves():
            return False
        if movekey == 'u':
            return [(self.__location[0] - 1, self.__location[1])]
        if movekey == 'd':
            return [(self.__location[0] + self.__length, self.__location[1])]

        if movekey == 'r':
            return [(self.__location[0], self.__location[1] + self.__length)]
        if movekey == 'l':
            return [(self.__location[0], self.__location[1] - 1)]

    def move(self, movekey):
        if movekey not in self.possible_moves():
            return False

        if movekey == "u":
            self.__location = (self.__location[0] - 1, self.__location[1])
            return True

        if movekey == "d":
            self.__location = (self.__location[0] + 1, self.__location[1])
            return True

        if movekey == "l":
            self.__location = (self.__location[0], self.__location[1] - 1)
            return True

        if movekey == "r":
            self.__location = (self.__location[0], self.__location[1] + 1)
            return True

    def get_name(self):
        return self.__name
