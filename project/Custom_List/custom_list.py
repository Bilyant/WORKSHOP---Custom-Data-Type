import sys
from copy import deepcopy


class ErrorMessages:
    invalid_data_type = 'Please provide a valid data type'
    out_of_range = 'The index is out of range'
    value_not_found = 'The value is not in the data structure'
    empty_data_structure = 'The data structure can not be empty'
    not_enough_values = 'Not enough values in the data structure'


class CustomDataStructure:
    def __init__(self):
        self.__values = []
        self.messages = ErrorMessages()

    def append(self, value):
        self.__values.append(value)
        return self.__values

    def remove(self, index):
        try:
            int(index)
        except ValueError:
            raise ValueError(self.messages.invalid_data_type)
        try:
            self.__values[index]
        except IndexError:
            raise ValueError(self.messages.value_not_found)
        return self.__values.pop(index)

    def get(self, index):
        try:
            self.__values[index]
        except IndexError:
            raise IndexError(self.messages.value_not_found)
        return self.__values[index]

    def extend(self, iterable):
        if iterable.__class__.__name__ != 'list':
            raise TypeError(self.messages.invalid_data_type)
        new_list = self.__values + iterable
        return new_list

    def insert(self, value, index=0):
        try:
            int(index)
        except ValueError:
            raise TypeError(self.messages.invalid_data_type)

        try:
            self.__values[index]
        except IndexError:
            raise ValueError(self.messages.out_of_range)

        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        try:
            self.__values[0]
        except IndexError:
            raise IndexError(self.messages.empty_data_structure)
        return self.__values.pop()

    def clear(self):
        if len(self.__values) == 0:
            raise ValueError(self.messages.empty_data_structure)
        self.__values.clear()

    def index(self, value):
        if value not in self.__values:
            raise ValueError(self.messages.value_not_found)
        return self.__values.index(value)

    def count(self, value):
        if value not in self.__values:
            raise ValueError(self.messages.value_not_found)
        return self.__values.count(value)

    def reverse(self):
        if len(self.__values) == 0:
            raise ValueError(self.messages.empty_data_structure)
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.__values.insert(0, value)

    def dictionize(self):
        res = {}
        for idx in range(0, len(self.__values), 2):
            if idx == len(self.__values) - 1 and idx % 2 == 0:
                res[self.__values[idx]] = ' '
                break
            res[self.__values[idx]] = self.__values[idx + 1]
        return res

    def move(self, amount: int):
        if not (isinstance(amount, int)):
            raise ValueError(self.messages.invalid_data_type)
        if amount > len(self.__values):
            raise ValueError(self.messages.not_enough_values)
        values = [self.__values[i] for i in range(amount)]
        for el in values:
            self.__values.pop(self.__values.index(el))
            self.__values.append(el)
        return self.__values

    def sum(self):
        result = 0
        for el in self.__values:
            if isinstance(el, int) or isinstance(el, float):
                result += el
            elif '__len__' in dir(el):
                result += len(el)
        return result

    def overbound(self):
        if len(self.__values) == 0:
            raise ValueError(self.messages.empty_data_structure)
        biggest_value_idx = 0
        biggest_value = -sys.maxsize
        for idx in range(len(self.__values)):
            if isinstance(self.__values[idx], int) or isinstance(self.__values[idx], float):
                if self.__values[idx] > biggest_value:
                    biggest_value_idx = idx
                    biggest_value = self.__values[idx]
            elif '__len__' in dir(self.__values[idx]):
                if self.__values[idx] > biggest_value:
                    biggest_value_idx = idx
        return biggest_value_idx

    def underbound(self):
        if len(self.__values) == 0:
            raise ValueError(self.messages.empty_data_structure)
        smallest_value_idx = 0
        smallest_value = sys.maxsize
        for idx in range(len(self.__values)):
            if isinstance(self.__values[idx], int) or isinstance(self.__values[idx], float):
                if self.__values[idx] < smallest_value:
                    smallest_value_idx = idx
                    smallest_value = self.__values[idx]
            elif '__len__' in dir(self.__values[idx]):
                if self.__values[idx] < smallest_value:
                    smallest_value_idx = idx
        return smallest_value_idx

    def __repr__(self):
        return f'{self.__values}'
