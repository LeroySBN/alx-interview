#!/usr/bin/python3
"""pascal_triangle.py
"""


def pascal_triangle(n):
    my_list = list()
    my_list_joined = list()

    if n <= 0:
        return my_list

    my_list.append(1)
    
    for i in range(n):
        if i > 0:
            my_list.append(0)
            new_list = list.copy(my_list)
            for j in range(1,i+1):
                new_list[j] = my_list[j] + my_list[j-1]
            my_list.clear()
            my_list = list.copy(new_list)
        my_list_joined.append(list(my_list))
        # print(my_list_joined)
    return my_list_joined

pascal_triangle(5)
