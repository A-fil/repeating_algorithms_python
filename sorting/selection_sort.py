from typing import List, Any

from test_data.sorting_data import UNSORTED_NUMERICAL_SEQUENCE


def selection_sort(target_list: List[Any]):
    """
    Insertion Sort algorithm
    Worst case O(n^2)
    :param target_list: Target to sort
    :return: Sorted list
    """

    target_length = len(target_list)

    for index in range(0, target_length):
        index_element = target_list[index]

        smallest_value = index_element
        smallest_index = index
        for subindex in range(index, target_length):
            subindex_element = target_list[subindex]
            if subindex_element < smallest_value:
                smallest_value = subindex_element
                smallest_index = subindex
        if smallest_index != index:
            target_list[index] = target_list[smallest_index]
            target_list[smallest_index] = index_element

    return target_list


print("Unsorted: {}".format(UNSORTED_NUMERICAL_SEQUENCE))
print("Sorted: {}".format(selection_sort(UNSORTED_NUMERICAL_SEQUENCE)))
