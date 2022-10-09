#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def proizv():
    print("Введите числa: ")
    proz = 1
    while True:
        a = int(input(">>> "))
        if a == 0:
            break
        else:
            proz *= a
    print("Итог: ", proz)


if __name__ == '__main__':
    proizv()
