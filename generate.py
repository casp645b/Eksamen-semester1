import Filter
import Network
import Comparator


def extend(w: list[Filter], n: int) -> list[Filter]:
    """

    """
    result = []
    stdComparators = Comparator.stdComparators(n)
    for f in w:
        for c in stdComparators:
            if not Filter.isRedundant(c, f):
                result = result + [Filter.add(c, f)]
    return result
    
    result = []
    stdComparators = Comparator.stdComparators(n)
    for f in w:
        nonRedundants = list(filter(lambda x: not Filter.isRedundant(x, f), stdComparators))
        result = result + list(map(lambda x: Filter.add(x, f), nonRedundants))
    return result
