from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    return list((x, y) for x in arr1 for y in arr2)
