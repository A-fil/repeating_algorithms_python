from typing import List, Any

from test_data.sorting_data import UNSORTED_NUMERICAL_SEQUENCE


def merge(target_list, start_index, split_index, end_index):
    left = target_list[start_index:split_index + 1]
    left.append(None)

    right = target_list[split_index + 1: end_index + 1]
    right.append(None)

    i = 0
    j = 0
    for index in range(start_index, end_index+1):
        if left[i] is None:
            target_list[index] = right[j]
            j = j + 1
        elif right[j] is None:
            target_list[index] = left[i]
            i = i + 1
        elif left[i] <= right[j]:
            target_list[index] = left[i]
            i = i + 1
        else:
            target_list[index] = right[j]
            j = j + 1


def merge_and_sort_range(target_list: List[Any], start_index: int, end_index: int):
    if start_index < end_index:
        split_index = int((start_index + end_index) / 2)
        merge_and_sort_range(target_list, start_index, split_index)
        merge_and_sort_range(target_list, split_index+1, end_index)
        merge(target_list, start_index, split_index, end_index)


def merge_sort(target_list: List[Any]):
    """
    Merge Sort algorithm
    Worst case O(n log n)
    :param target_list: Target to sort
    :return: Sorted list
    """

    target_length = len(target_list)
    merge_and_sort_range(target_list, 0, target_length - 1)
    return target_list


print("Unsorted: {}".format(UNSORTED_NUMERICAL_SEQUENCE))
print("Sorted: {}".format(merge_sort(UNSORTED_NUMERICAL_SEQUENCE)))
