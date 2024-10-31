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
    """
    return Network([])

def append(c: Comparator.Comparator, net: Network) -> Network:
    """
        Adds a comparator to the end of the network
    """
    net.comparators.append(c)
    return net

def size(net: Network) -> int:
    """
        Returns the amount of comparators in the network
    """
    return len(net.comparators)

def maxChannel(net: Network) -> int:
    """
        Returns the largest channel the network can affect

        Function cannot take empty networks
    """
    return max(map(Comparator.maxChannel, net.comparators))


def isStandard(net: Network) -> bool:
    """
        Returns true if all comparators in the network are "Standard"
        else returns false
    """
    return list(filter(Comparator.isStandard, net.comparators)) == net.comparators


def apply(net: Network, w: list[int]) -> list[int]:
    """
        Applies the comparators in a network to the list w
    """
    return list(functools.reduce(lambda x, y: Comparator.apply(y, x), net.comparators, w))


def outputs(net: Network, w: list[list[int]]) -> list[list[int]]:
    """
        Returns a list of unique lists as a result of net being applied to the lists in w
    """
    v = list(map(lambda x: apply(net, x), w))
    return list(map(lambda x: v[x], filter(lambda x: not member(v[x], v[x+1:]), range(len(v)))))

def member(x: any, v: list) -> bool:
    """
        Returns the truthvalue for wether or not x is a part of v
        Purpose is to help outputs function
    """
    return list(filter(lambda y: x == y, v)) != []


def allOutputs(net: Network, n: int) -> list[list[int]]:
    """
        Returns the output of the outputs function for all binary permutations of a list with length n
    """
    v = list(map(lambda x: baseTenToBinary(x, n), range(2**n)))
    return outputs(net, v)


def baseTenToBinary(m: int, n: int) -> list[int]:
    """
        Converts a base ten number m to a list reprecenting its binary value
        of length n
        Purpose is to help allOutputs function
        
        m must be less than 2^n
        
        >>>baseTenToBinary(29, 7)
        [0, 0, 1, 1, 1, 0, 1]
    """
    v = list(map(lambda x: pow(2, x), range(n-1, -1, -1)))
    return list(map(lambda x: (m//v[x])%2, range(n)))


def funktionis_sorting(net: Network, size: int) -> bool:
    """
        Check wether or not a given network will correctly sort all lists of length size

        The maximum channel the network refers to must be less than the size for this function to be used
    """
    return len(allOutputs(net, size)) == size + 1
