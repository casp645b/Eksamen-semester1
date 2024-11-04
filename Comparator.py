from dataclasses import dataclass

@dataclass
class Comparator:
    """
        Dataclass that contains the position of 2 integers to compare
    """
    channel1: int
    channel2: int


def makeComparator(i: int, j: int) -> Comparator:
    """
        Creates a new instance of comparator.
        
        i and j can not be the same

        >>> makeComparator(0, 1)
        Comparator(channel1=0, channel2=1)
    """
    return Comparator(i, j)


def minChannel(c: Comparator) -> int:
    """        
        Returns the channel the lowest value is to be put by the comparator
        
        >>> minChannel(makeComparator(1,0))
        0
    """
    return c.channel1 if c.channel1 < c.channel2 else c.channel2


def maxChannel(c: Comparator) -> int:
    """        
        Returns the channel the highest value is to be put by the comparator
        
        >>> maxChannel(makeComparator(1,0))
        1
    """
    return c.channel1 if c.channel1 > c.channel2 else c.channel2


def isStandard(c: Comparator) -> bool:
    """
        Returns whether or not the comparator is standard.
        I.e. if it outputs the smallest value on the smallest channel
        
        >>> isStandard(makeComparator(1,0))
        False
    """
    return (c.channel1 == minChannel(c) and c.channel2 == maxChannel(c))


def apply(c: Comparator, w: list[int]) -> list[int]:
    """
        Applies a comparator on the list w
        I.e. compares two values on w as specified in the comparator and sorts them

        maxChannel of c has to be less than the length of w
        
        >>> apply(makeComparator(1,0), [2, 1, 3])
        [1, 2, 3]
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
        Returns a list with all possible comparators with different channels
        for n total channels
        
        >>> allComparators(2)
        [Comparator(channel1=0, channel2=1), Comparator(channel1=1, channel2=0)]
    """
    v = []
    for i in range(n):
        for j in range(n):
            if (i != j):
                v.append(makeComparator(i,j))
    return v


def stdComparators(n: int) -> list[Comparator]:
    """
        Returns a list with all standard comparator for n total channels

        >>> stdComparators(2)
        [Comparator(channel1=0, channel2=1)]
    """
    return list(filter(isStandard, allComparators(n)))


def toProgram(c: Comparator, var: str, aux: str) -> list[str]:
    """
        Returns a list of strings that, if insertet in  Python shell,
        sorts a list with name var based on instructions in comparator

        Does not use the variable aux

        >>> toProgram(makeComparator(0, 1), "a", "b")
        ['c = makeComparator(0, 1)', 'i = 0', 'j = 1', 'if a[i] < a[j]:', \
'  if not isStandard(c):', '    a[i], a[j] = a[j], a[i]', 'else:', \
'  if isStandard(c):', '    a[i], a[j] = a[j], a[i]']
    """
    return [f"c = makeComparator({c.channel1}, {c.channel2})",
            f"i = {c.channel1}",
            f"j = {c.channel2}",
            f"if {var}[i] < {var}[j]:",
            f"  if not isStandard(c):",
            f"    {var}[i], {var}[j] = {var}[j], {var}[i]",
            f"else:",
            f"  if isStandard(c):",
            f"    {var}[i], {var}[j] = {var}[j], {var}[i]"]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
