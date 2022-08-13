from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    regex = re.compile(r'\w+')
    words_len = regex.findall(text)
    max_len = max(words_len, key=len, default=None)
    min_len = min(words_len, key=len, default=None)
    return min_len, max_len
