#!/usr/bin/python
# -*- coding: utf-8 -*-

import chet_nechet

formula = raw_input('Введите функцию переменной x ')
code = """
def f(x):
    return %s
""" % formula
#exec(code)
if chet_nechet.chet(code)==2:
    print('Функция явл чётной')
elif chet_nechet.nechet(code)==1:
    print('Функция явл нечётной')
else:
    print('Функция явл ни чётной, ни нечётной')

