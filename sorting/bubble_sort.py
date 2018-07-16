from typing import List, Any

from test_data.sorting_data import UNSORTED_NUMERICAL_SEQUENCE
from utils.array_utils import swap


def bubble_sort(target_list: List[Any]):
    """
    Bubble Sort algorithm
    Worst case O(n^2)
    :param target_list: Target to sort
    :return: Sorted list
    """

    target_length = len(target_list)

    for index in range(0, target_length):
        for subindex in range(target_length - 1, index - 1, -1):
            if target_list[subindex] < target_list[subindex - 1]:
                swap(target_list, subindex, subindex - 1)

    return target_list


print("Unsorted: {}".format(UNSORTED_NUMERICAL_SEQUENCE))
print("Sorted: {}".format(bubble_sort(UNSORTED_NUMERICAL_SEQUENCE)))
