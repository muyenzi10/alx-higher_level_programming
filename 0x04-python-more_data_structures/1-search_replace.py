#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for data in my_list:
        if data == search:
            new.append(replace)
        else:
            new.append(data)
    return new
