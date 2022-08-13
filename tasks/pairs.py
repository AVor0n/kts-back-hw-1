from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    return list(zip(arr1, arr2))
