#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    n1_list = []
    for i in range(list_length):
        try:
            rs = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            rs = 0
        except ZeroDivisionError:
            print("division by 0")
            rs = 0
        except IndexError:
            print("out of range")
            rs = 0
        finally:
            n1_list.append(r)
    return n1_list
