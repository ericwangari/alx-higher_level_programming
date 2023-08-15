#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all mutiples od 2 in a list."""
    mutiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mutiples.append(True)
        else:
            mutiples.append(False)

    return (multiples)
