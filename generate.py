import filter
import network
import comparator


def extend(w: list[filter.Filter], n: int) -> list[filter.Filter]:
    """

    """
    result = []
    std_comparators = comparator.std_comparators(n)
    for f in w:
        for c in std_comparators:
            if not filter.is_redundant(c, f):
                result = result + [filter.add(c, f)]
    return result
    
    result = []
    std_comparators = comparator.std_comparators(n)
    for f in w:
        nonRedundants = list(filter(lambda x: not filter.is_redundant(x, f), std_comparators))
        result = result + list(map(lambda x: filter.add(x, f), nonRedundants))
    return result
