#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def circle(r):
    return math.pi * r ** 2


def cylinder():
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    s = 2 * math.pi * r * h

    zapr = int(input("Если Вы хотите получить площадь бок. повер. введите 1, если полную площадь то 2: "))
    if zapr == 1:
        print(s)

    elif zapr == 2:
        print(s + (circle(r) * 2))


if __name__ == '__main__':
    cylinder()
