from dataclasses import dataclass, field
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
    return list(tuple(map(lambda x: apply(net, x), w)))
