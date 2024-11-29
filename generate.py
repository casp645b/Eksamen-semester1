import filter
import network
import comparator


def extend(w: list[filter.Filter], n: int) -> list[filter.Filter]:
    """
        Makes a copy of each filter in w
        and extends each of them by a non-redundant comparator in all possible ways
        Returns a list consisting of the filters
        where a non-redundant comparator is added

        The length of the binary permutations in the binary output 
        in each filter in w must be equal to n.

        >>> extend([filter.make_empty_filter(3)], 3)
        [Filter(netw=Network(comparators=[Comparator(channel1=0, channel2=1)]), \
binaryOut=[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]), \
Filter(netw=Network(comparators=[Comparator(channel1=0, channel2=2)]), \
binaryOut=[[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]), \
Filter(netw=Network(comparators=[Comparator(channel1=1, channel2=2)]), \
binaryOut=[[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]])]
    """
    result = []
    stdComparators = comparator.std_comparators(n)
    for f in w:
        for c in stdComparators:
            if not filter.is_redundant(c, f):
                result = result + [filter.add(c, f)]
    return result
    
    result = []
    stdComparators = comparator.std_comparators(n)
    for f in w:
        nonRedundants = list(filter(lambda x: not filter.is_redundant(x, f),
                                    stdComparators))
        result = result + list(map(lambda x: filter.add(x, f), nonRedundants))
    return result

    result = []
    nChannelFilters = list(map(lambda x: filter.Filter(filter.net(x), network.all_outputs(net(x), n), w)))
    stdComparators = comparator.std_comparators(n)
    for f in w:
        for c in stdComparators:
            if not filter.is_redundant(c, f):
                result = result + [filter.add(c, f)]
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
