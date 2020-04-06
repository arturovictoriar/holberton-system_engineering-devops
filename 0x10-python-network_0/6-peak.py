#!/usr/bin/python3
"""
    Find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if list_of_integers:
        peak = list_of_integers[0]
    else:
        return None

    for i, num in enumerate(list_of_integers):
        if num >= list_of_integers[len(list_of_integers) - 1 - i]:
            max_num = num
        else:
            max_num = list_of_integers[len(list_of_integers) - 1 - i]

        if max_num > peak:
            peak = max_num

        if (len(list_of_integers) // 2) - i <= 0:
            break

    return peak
