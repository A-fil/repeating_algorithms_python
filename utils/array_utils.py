from typing import List, Any


def swap(array: List[Any], index1: int, index2: int):
    temporary = array[index1]
    array[index1] = array[index2]
    array[index2] = temporary
