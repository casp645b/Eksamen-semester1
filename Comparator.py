from dataclasses import dataclass

@dataclass
class Comparator:
    """
        Dataclass that contains 2 integers to compare
    """
    channel1: int
    channel2: int


def makeComparator(i: int, j: int) -> Comparator:
    """
        Creates a new instance of comparator
    """
    return Comparator(i, j)


def minChannel(c: Comparator) -> int:
    """        
        Returns the channel the lowest value is to be put by the comparator
        >>>minChannel(makeComparator(1,0))
        0
    """
    return c.channel1 if c.channel1 < c.channel2 else c.channel2


def maxChannel(c: Comparator) -> int:
    """        
        Returns the channel the highest value is to be put by the comparator
        >>>maxChannel(makeComparator(1,0))
        1
    """
    return c.channel1 if c.channel1 > c.channel2 else c.channel2


def isStandard(c: Comparator) -> bool:
    """
        Returns wether or not the comparator is standard.
        I.e. if it outputs the smallest value on the smallest channel
        >>>isStandard(makeComparator(1,0))
        false
    """
    return (c.channel1 == minChannel(c) and c.channel2 == maxChannel(c)
            and c.channel1 != c.channel2)


def apply(c: Comparator, w: list[int]) -> list[int]:
    """
        Applies a comparator on the list w
        I.e. compares two values on w as specified in the comparator and sorts them
        >>>apply(makeComparator(1,0), [2,1,3])
        [1,2,3]
    """
    if w[c.channel1] < w[c.channel2]:
        if not isStandard(c):
            w[c.channel1], w[c.channel2] = w[c.channel2], w[c.channel1]
        return w
    else:
        if isStandard(c):
            w[c.channel1], w[c.channel2] = w[c.channel2], w[c.channel1]
        return w


def allComparators(n: int) -> list[Comparator]:
    """
        Returns a list with all possible comparators
        >>>allComparators(2)
        [comparator(channel1=0, channel2=0), comparator(channel1=0, channel2=1),
        comparator(channel1=1, channel2=0), comparator(channel1=1, channel2=1)]
    """
    v = list(range(n**2))
    for i in range(n):
        for j in range(n):
            v[i*n+j] = makeComparator(i,j)
    return v


def stdComparators(n: int) -> list[Comparator]:
    """
        Returns a list with all standard comparator
    """
    return list(filter(isStandard, allComparators(n)))
