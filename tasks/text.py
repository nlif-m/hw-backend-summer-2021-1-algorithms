from types import MappingProxyType
from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    words = list(map(lambda x: x.strip(), text.split()))
    if len(words) < 2:
        return (None, None)
    result = ["", ""]
    if len(words[0]) >= len(words[1]):
        result[0] = words[1]
        result[1] = words[0]
    else:
        result[0] = words[0]
        result[1] = words[1]

    for word in words[2:]:
        word_len = len(word)
        if word_len < len(result[0]):
            result[0] = word
        if word_len > len(result[1]):
            result[1] = word
    
    return tuple(result)
