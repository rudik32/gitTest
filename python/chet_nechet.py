#!/usr/bin/python
# -*- coding: utf-8 -*-

def chet(x):
    """Проверяет, является ли функция чётной"""
    exec(x)
    if f(1) == f(-1):
	return 2
    else:
	return 0
def nechet(x):
    """Проверяет, является ли функция нечётной"""
    exec(x)
    if f(-1) == -1*f(1):
	return 1
    else:
	return 0

if __name__ == "__main__":
    chet(x)
    nechet(x)