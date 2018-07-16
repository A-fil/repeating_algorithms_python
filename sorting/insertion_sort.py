from typing import List, Any

from test_data.sorting_data import UNSORTED_NUMERICAL_SEQUENCE


def insertion_sort(target_list: List[Any]):
    """
    Insertion Sort algorithm
    Worst case O(n^2)
    :param target_list: Target to sort
    :return: Sorted list
    """

    target_length = len(target_list)

    for index in range(1, target_length):
        key = target_list[index]
        # Insert target_list[index] into the sorted sequence target_list[0...target_length-1]

        subindex = index - 1
        while subindex >= 0 and target_list[subindex] > key:
            target_list[subindex + 1] = target_list[subindex]
            subindex = subindex - 1
        target_list[subindex + 1] = key

    return target_list

print("Unsorted: {}".format(UNSORTED_NUMERICAL_SEQUENCE))
print("Sorted: {}".format(insertion_sort(UNSORTED_NUMERICAL_SEQUENCE)))
