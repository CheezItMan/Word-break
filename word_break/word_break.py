from typing import List, Set
from heapq import heappush, heappop


def word_break(s: str, word_dict: Set[str]) -> bool:
    # Memo stores the fact that the substring ending at the given index,
    # is in the dictionary or not.
    memo = [False for _ in range(len(s) + 1)]
    #  The empty string is always in the dictionary.
    memo[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):  # from 0 to i-1
            if memo[j] and s[j:i] in word_dict:
                memo[i] = True
                break

    return memo[len(s)]
