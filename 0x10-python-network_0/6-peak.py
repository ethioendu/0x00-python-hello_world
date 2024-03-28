#!/usr/bin/python3
'''a function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''Helper function to get the element at index i,
    returns float('-inf') for out of bounds indices.'''
    def get_element(i):
        if 0 <= i < len(list_of_integers):
            return list_of_integers[i]
        return float('-inf')

    left, right = 0, len(list_of_integers) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = list_of_integers[mid]
        prev_element = get_element(mid - 1)
        next_element = get_element(mid + 1)

        if mid_element >= prev_element and mid_element >= next_element:
            return mid_element
        elif mid_element < prev_element:
            right = mid - 1
        else:
            left = mid + 1

    return None
