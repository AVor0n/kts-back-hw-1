__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    sum_even = sum(list(filter(lambda i: not i % 2, arr)))
    sum_odd = sum(list(filter(lambda i: i % 2, arr)))
    if sum_odd == 0:
        return 0
    return sum_even / sum_odd
