#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def sort_decorator(func):
    def wrapper():
        numbers = func()
        numbers.sort()
        return numbers
    return wrapper


@sort_decorator
def get_list():
    number_string = input("Введите строку чисел через пробел: ")
    number_list = [int(number) for number in number_string.split()]
    return number_list


if __name__ == "__main__":
    sorted_list = get_list()
    print(sorted_list)
