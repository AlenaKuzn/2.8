#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    stroka = input("Введите строку: ")
    return stroka


def test_input(stroka):
    if type(stroka) == int:
        return True
    elif stroka.isnumeric():
        return True
    else:
        return False


def str_to_int(stroka):
    a = int(stroka)
    return a


def print_int(stroka):
    print(stroka)


if __name__ == '__main__':
    stroka = get_input()
    proverka = test_input(stroka)
    if proverka is True:
        print_int(str_to_int(stroka))
    else:
        print("Введённая строка не является числом")
