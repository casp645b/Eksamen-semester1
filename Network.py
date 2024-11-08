from dataclasses import dataclass
import Comparator
import functools

@dataclass
class Network:
    """
        Class that contains a list of comparators to use
    """
    comparators: list[Comparator.Comparator]


def emptyNetwork() -> Network:
    """
        Creates a new empty instance of network

        >>> emptyNetwork()
        Network(comparators=[])
    """
    return Network([])

def append(c: Comparator.Comparator, net: Network) -> Network:
    """
        Adds a comparator to the end of the network

        >>> append(Comparator.makeComparator(0, 1), emptyNetwork())
        Network(comparators=[Comparator(channel1=0, channel2=1)])
    """
    net.comparators.append(c)
    return net

def size(net: Network) -> int:
    """
        Returns the amount of comparators in the network

        >>> size(append(Comparator.makeComparator(0, 1), emptyNetwork()))
        1
    """
    return len(net.comparators)

def maxChannel(net: Network) -> int:
    """
        Returns the largest channel the network can affect

        Function cannot take empty networks

        >>> maxChannel(append(Comparator.makeComparator(0, 1), emptyNetwork()))
        1
    """
    return max(map(Comparator.maxChannel, net.comparators))


def isStandard(net: Network) -> bool:
    """
        Returns true if all comparators in the network are "Standard"
        else returns false

        >>> isStandard(append(Comparator.makeComparator(0, 1), emptyNetwork()))
        True
    """
    return list(filter(Comparator.isStandard, net.comparators)) == net.comparators


def apply(net: Network, w: list[int]) -> list[int]:
    """
        Applies the comparators in a network to the list w

         the length of w has to greater than maxChannel of net
        >>> apply(append(Comparator.makeComparator(0, 1), emptyNetwork()), [3, 2, 1])
        [2, 3, 1]
    """
    return list(functools.reduce(lambda x, y: Comparator.apply(y, x),
                                 net.comparators, w))


def outputs(net: Network, w: list[list[int]]) -> list[list[int]]:
    """
        Returns a list of unique lists (i.e. removes duplicates)
        as a result of net being applied to the lists in w

        the length of each element of w must be greater than maxChannel of net

        >>> outputs(append(Comparator.makeComparator(0, 1),
        ... emptyNetwork()), [[3, 2, 1], [2, 3, 1], [2, 1, 3]])
        [[2, 3, 1], [1, 2, 3]]
    """
    v = list(map(lambda x: apply(net, x), w))
    index=list(filter(lambda x: not member(v[x], v[x+1:]), range(len(v))))
    return list(map(lambda x: v[x], index))

def member(x: any, v: list) -> bool:
    """
        Returns the truthvalue for whether or not x is a part of v
        Purpose is to help outputs function

        >>> member(2, [1, 2, 3])
        True
    """
    return list(filter(lambda y: x == y, v)) != []


def allOutputs(net: Network, n: int) -> list[list[int]]:
    """
        Returns the output of the outputs function
        for all binary permutations of a list with length n

        n has to be greater than maxChannel of net

        >>> allOutputs(append(Comparator.makeComparator(0, 1), emptyNetwork()), 3)
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]
    """
    v = list(map(lambda x: baseTenToBinary(x, n), range(2**n)))
    return outputs(net, v)


def baseTenToBinary(m: int, n: int) -> list[int]:
    """
        Converts a base ten number m to a list reprecenting its binary value
        of length n
        Purpose is to help allOutputs function
        
        m must be less than 2^n
        
        >>> baseTenToBinary(29, 7)
        [0, 0, 1, 1, 1, 0, 1]
    """
    v = list(map(lambda x: pow(2, x), range(n-1, -1, -1)))
    return list(map(lambda x: (m//v[x])%2, range(n)))


def isSorting(net: Network, size: int) -> bool:
    """
        Check whether or not a the comparatornetwork net 
        is a sorting network to size inputs,
        i.e check whether or not net will correctly sort all lists of length size
        

        
        size must be greather then The maximum channel the network refers to 
        for this function to be used

        >>> isSorting(append(Comparator.makeComparator(0, 1), emptyNetwork()), 3)
        False

        >>> isSorting(append(Comparator.makeComparator(0, 1), emptyNetwork()), 2)
        True
    """
    return len(allOutputs(net, size)) == size + 1


def toProgram(net: Network, var: str, aux: str) -> list[str]:
    """
        Returns a list of strings that, if insertet in  Python shell,
        sorts a list with name var based on instructions in network

        Does not use the variable aux

        >>> toProgram(append(Comparator.makeComparator(0, 1), emptyNetwork()),
        ... "a", "b")
        ['c = makeComparator(0, 1)', 'i = 0', 'j = 1', 'if a[i] < a[j]:', \
'  if not isStandard(c):', '    a[i], a[j] = a[j], a[i]', 'else:', \
'  if isStandard(c):', '    a[i], a[j] = a[j], a[i]']

        >>> toProgram(append(Comparator.makeComparator(1, 2),
        ... append(Comparator.makeComparator(0, 1), emptyNetwork())), "a", "b")
        ['c = makeComparator(0, 1)', 'i = 0', 'j = 1', 'if a[i] < a[j]:', \
'  if not isStandard(c):', '    a[i], a[j] = a[j], a[i]', 'else:', \
'  if isStandard(c):', '    a[i], a[j] = a[j], a[i]', 'c = makeComparator(1, 2)', \
'i = 1', 'j = 2', 'if a[i] < a[j]:', '  if not isStandard(c):', \
'    a[i], a[j] = a[j], a[i]', 'else:', '  if isStandard(c):', \
'    a[i], a[j] = a[j], a[i]']
    """
    return list(functools.reduce(lambda x, y: x+y,
                                 map(lambda x: Comparator.toProgram(x, var, aux),
                                     net.comparators), []))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
