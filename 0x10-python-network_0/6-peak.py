#!/usr/bin/python3
"""
This function implements a binary search algorithm to
find a peak in a list of unsorted integers.
With a time complexity of O(log(n)).
"""


def find_peak(list_of_integers):
    """
    ARGS:
        mid_element, mid_index, right_half, left_half.
    """

    if list_of_integers:
        if all(element == list_of_integers[0] for
               element in list_of_integers):
            return list_of_integers[0]

    if len(list_of_integers) == 0:
        return None

    elif len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]

    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_index = len(list_of_integers) // 2
    mid_element = list_of_integers[mid_index]
    if mid_index - 1 >= 0 and mid_index + 1 < len(list_of_integers):
        if mid_element >= list_of_integers[mid_index - 1] and \
           mid_element >= list_of_integers[mid_index + 1]:
            return mid_element

    if mid_index + 1 < len(list_of_integers) and \
       mid_element < list_of_integers[mid_index + 1]:
        right_half = list_of_integers[mid_index + 1:]
        peak = find_peak(right_half)
        return peak

    if mid_element < list_of_integers[mid_index - 1]:
        left_half = list_of_integers[: mid_index]
        peak = find_peak(left_half)
        return peak
