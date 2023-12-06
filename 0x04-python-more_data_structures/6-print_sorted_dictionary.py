#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    for i in dict_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
