# IN PROGRESS

from typing import List, Any

from test_data.sorting_data import UNSORTED_NUMERICAL_SEQUENCE
from utils.array_utils import swap


def parent_index(index: int):
    return int((index - 1) / 2)


def left_index(index: int):
    return 2 * index + 1


def right_index(index: int):
    return 2 * index + 2


def build_max_heap(target_list: List[Any], heap_size: int, root_index: int):
    start = parent_index(heap_size)

    if left <=

def heap_sort(target_list: List[Any]):
    """
    Bubble Sort algorithm
    Worst case O(n^2)
    :param target_list: Target to sort
    :return: Sorted list
    """
    heap_size = len(target_list)
    for i in range(int(heap_size / 2 - 1), -1, -1):
        build_max_heap(target_list, heap_size, i)

    for i in range(int(heap_size - 1), -1, -1):
        swap(target_list, 0, i)

        build_max_heap(target_list, i, 0)

    build_max_heap(target_list)
    return target_list


print("Unsorted: {}".format(UNSORTED_NUMERICAL_SEQUENCE))
print("Sorted: {}".format(heap_sort(UNSORTED_NUMERICAL_SEQUENCE)))
