from test_lib import test, report
from math import floor, ceil, pow

nr = 5.65499901
expected = 5.65
calculated = round(nr,2)
test('example', expected, calculated)

nr = 13
expected = 13.0
calculated = float(nr) 
test('to-the-point',expected, calculated)

nr = -45.372
expected = 45.372
calculated = abs(nr)
test('optimistic', expected, calculated)

nr = -45.372
expected = -45.4
calculated = round(nr, 1) 
test('approximately', expected, calculated)

nr = -45.372
expected = 45.372
calculated = abs(nr) 
test('pessimistic', expected, calculated)

nr = -2.3
expected = -3
calculated = floor(nr) 
test('depressed', expected, calculated)

nr = int(-7.25)
expected = -7
calculated = round(nr, 2) 
test('pointless', expected, calculated)

nr = 15.11
expected = 16
calculated = ceil(nr) 
test('sky-is-the-limit', expected, calculated)

nr = -133.4447
expected = 133.445
calculated = round(abs(nr), 3)
test('cjv6', expected, calculated)



report()



