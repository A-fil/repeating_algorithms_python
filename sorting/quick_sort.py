from typing import List, Any

from test_data.sorting_data import UNSORTED_NUMERICAL_SEQUENCE
from utils.array_utils import swap


def partition(target_list, start_index, end_index) -> int:
    pivot_element = target_list[end_index] # Can be choosen different ways
    lower_partition_roof = start_index - 1
    for j in range(start_index, end_index - 2):
        if target_list[j] <= pivot_element:
            lower_partition_roof = lower_partition_roof + 1
            swap(target_list, lower_partition_roof, j)
    swap(target_list, lower_partition_roof + 1, end_index)
    return lower_partition_roof + 1


def apply_quicksort(target_list: List[Any], start_index: int, end_index: int):
    if start_index < end_index:
        split_index = partition(target_list, start_index, end_index)
        apply_quicksort(target_list, start_index, split_index - 1)
        apply_quicksort(target_list, split_index + 1, end_index)


def quick_sort(target_list: List[Any]):
    """
    Merge Sort algorithm
    Worst case O(n log n)
    :param target_list: Target to sort
    :return: Sorted list
    """

    target_length = len(target_list)
    apply_quicksort(target_list, 0, target_length - 1)
    return target_list


print("Unsorted: {}".format(UNSORTED_NUMERICAL_SEQUENCE))
print("Sorted: {}".format(quick_sort(UNSORTED_NUMERICAL_SEQUENCE)))
