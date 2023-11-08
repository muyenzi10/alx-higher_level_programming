#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    arr = set(my_list)
    for i in arr:
        sum += i
    return sum
