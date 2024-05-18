"""
Algorithms for complicated yaml generation.
"""

from typing import Optional, List
import random
from collections import deque


def random_dfs_pool_select(pools: List[List[int]]) -> Optional[List[int]]:
    # Assumes items appear only once in each pool
    if not pools:
        return []

    # Sorting the pools to make selections smallest-pool-first gives a humongous speed improvement
    # Retain enough information to return to the original pool ordering for the return value.
    sort_indices = sorted(range(len(pools)), key=lambda x: len(pools[x]))
    unsort_indices = {sort_index: x for x, sort_index in enumerate(sort_indices)}
    pools = [pools[x] for x in sort_indices]

    # True means the option is available for selection; False means unavailable
    flags: List[List[bool]] = [[True for _ in x] for x in pools]
    selections: List[int] = deque(maxlen=len(pools))

    def set_flags(from_pool_index: int, value: int, set_value: bool) -> None:
        for pool_index in range(from_pool_index, len(flags)):
            pool = pools[pool_index]
            flag = flags[pool_index]
            for item_index, item in enumerate(pool):
                if item == value:
                    flag[item_index] = set_value
                    break

    pool_index = 0
    while pool_index < len(pools):
        if pool_index < 0:
            # We recursed all the way up; no solutions exist
            return None
        if len(selections) > pool_index:
            # We're reselecting when we've been here before; clear the flags
            set_flags(pool_index + 1, selections.pop(), set_value=True)
        weights = flags[pool_index]
        if sum(weights) == 0:
            # We tried everything on this layer, recurse up
            pool_index -= 1
            continue
        pool = pools[pool_index]
        selection = random.choices(pool, weights=weights)[0]
        set_flags(pool_index, selection, set_value=False)
        selections.append(selection)
        pool_index += 1
    return [selections[unsort_indices[index]] for index in range(len(selections))]
