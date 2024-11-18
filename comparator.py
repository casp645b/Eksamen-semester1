from dataclasses import dataclass

@dataclass
class Comparator:
    """
        Dataclass that contains the position of 2 integers to compare
    """
    channel1: int
    channel2: int


def make_comparator(i: int, j: int) -> Comparator:
    """
        Creates a new instance of comparator.
        
        i and j both must be non-negative and can not be the same

        >>> make_comparator(0, 1)
        Comparator(channel1=0, channel2=1)
    """
    return Comparator(i, j)


def min_channel(c: Comparator) -> int:
    """        
        Returns the channel the lowest value is to be put by the comparator
        
        >>> min_channel(make_comparator(1,0))
        0
    """
    return c.channel1 if c.channel1 < c.channel2 else c.channel2


def max_channel(c: Comparator) -> int:
    """        
        Returns the channel the highest value is to be put by the comparator
        
        >>> max_channel(make_comparator(1,0))
        1
    """
    return c.channel1 if c.channel1 > c.channel2 else c.channel2


def is_standard(c: Comparator) -> bool:
    """
        Returns whether or not the comparator is standard.
        I.e. if it outputs the smallest value on the smallest channel
        
        >>> is_standard(make_comparator(1,0))
        False
    """
    return c.channel1 == min_channel(c)


def apply(c: Comparator, w: list[int]) -> list[int]:
    """
        Applies a comparator on the list w
        I.e. compares two values on w as specified in the comparator and sorts them

        maxChannel of c must be less than the length of w
        
        >>> apply(make_comparator(1,0), [2, 1, 3])
        [1, 2, 3]
    """
    v = w.copy()
    if v[c.channel1] < v[c.channel2]:
        if not is_standard(c):
            v[c.channel1], v[c.channel2] = v[c.channel2], v[c.channel1]
        return v
    else:
        if is_standard(c):
            v[c.channel1], v[c.channel2] = v[c.channel2], v[c.channel1]
        return v


def all_comparators(n: int) -> list[Comparator]:
    """
        Returns a list of all possible comparators on n channels

        n must be positive
        
        >>> all_comparators(2)
        [Comparator(channel1=0, channel2=1), Comparator(channel1=1, channel2=0)]
    """
    v = []
    for i in range(n):
        for j in range(n):
            if (i != j):
                v.append(make_comparator(i,j))
    return v


def std_comparators(n: int) -> list[Comparator]:
    """
        Returns a list with all standard comparator for n total channels

        n must be positive

        >>> std_comparators(2)
        [Comparator(channel1=0, channel2=1)]
    """
    return list(filter(is_standard, all_comparators(n)))


def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
        Returns a list of strings that, if inserted in  Python shell,
        sorts a list with name var based on instructions in comparator

        Does not use the variable aux

        >>> to_program(make_comparator(0, 1), "a", "b")
        ['c = make_comparator(0, 1)', 'i = 0', 'j = 1', 'if a[i] < a[j]:', \
'  if not is_standard(c):', '    a[i], a[j] = a[j], a[i]', 'else:', \
'  if is_standard(c):', '    a[i], a[j] = a[j], a[i]']
    """
    return [f"c = make_comparator({c.channel1}, {c.channel2})",
            f"i = {c.channel1}",
            f"j = {c.channel2}",
            f"if {var}[i] < {var}[j]:",
            f"  if not is_standard(c):",
            f"    {var}[i], {var}[j] = {var}[j], {var}[i]",
            f"else:",
            f"  if is_standard(c):",
            f"    {var}[i], {var}[j] = {var}[j], {var}[i]"]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
