from math import factorial


def combinatins(a: int, b: int) -> int:
    return int(factorial(a) / (factorial(a - b) * factorial(b)))
