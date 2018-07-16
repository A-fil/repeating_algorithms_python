from typing import List
import random

random.seed = 100
test_data = [int(random.uniform(-100, 100)) for x in range(0, 100)]


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


# Optimal worst-case scenario
# Idea: Lets sort the array with a custom comparator

def comparator(a: int, b: int) -> int:
    if abs(a) == abs(b):
        return -1 if a < b else 1
    else:
        return -1 if abs(a) < abs(b) else 1


def optimal_worst_case_solution(values: List[int]) -> List[int]:
    sorted_list = sorted(values, key=cmp_to_key(comparator))

    sublist = []
    for index, value in enumerate(sorted_list):
        if index > 0 and value != 0 and sorted_list[index - 1] == -value:
            sublist.append(value)

    return sublist


print("Optimal worst case solution:")
print("Original list: {}".format(test_data))
print("Sought sublist: {}".format(optimal_worst_case_solution(test_data)))


# Optimal average case performance
# Idea: Use Hash-Map to store values
def optimal_average_case(values: List[int]) -> List[int]:
    hashed_storage = {}
    sublist = []
    for value in values:
        if value == 0:
            continue

        key = abs(value)

        if key in hashed_storage.keys():
            if hashed_storage[key] == -1*value:
                # Match
                sublist.append(key)
                hashed_storage[key] = 0
        else:
            hashed_storage[key] = value

    return sublist


print("Optimal average case solution:")
print("Original list: {}".format(test_data))
print("Sought sublist: {}".format(sorted(optimal_average_case(test_data)))) # Sorted to make it easier to compare

