from dataclasses import dataclass
import Comparator
import Network

@dataclass
class Filter:
    """

    """
    netw: Network.Network
    binaryOut: list[list[int]]

def makeEmptyFilter(n: int) -> Filter:
    """


        n must be greater than 1
    """
    return Filter(Network.emptyNetwork(), Network.allOutputs(Network.emptyNetwork(), n))

def net(f: Filter) -> Network.Network:
    """

    """
    return f.netw

def out(f: Filter) -> list[list[int]]:
    """

    """
    return f.binaryOut

def tempNet(c: Comparator.Comparator) -> Network.Network:
    """
        Returns a network with only one element, namely c

        Used as helping function in multiple functions
    """
    return Network.append(c, Network.emptyNetwork())

def isRedundant(c: Comparator.Comparator, f: Filter) -> bool:
    """
        
    """
    return len(out(f)) == len(Network.outputs(tempNet(c), out(f)))

def add(c: Comparator.Comparator, f: Filter) -> Filter:
    """
        Updates filter f by adding comparator c
        i.e. adds a comparator c to the network in f and updates binaryOut in f to reflect this change
    """
    Network.append(c, net(f))
    f.binaryOut = Network.outputs(tempNet(c), out(f))
    return f
