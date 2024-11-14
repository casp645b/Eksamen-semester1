from dataclasses import dataclass
import Comparator
import Network

@dataclass
class Filter:
    """
        Class that contains a network of comparators as well as all the binary outputs of said network
    """
    netw: Network.Network
    binaryOut: list[list[int]]

def makeEmptyFilter(n: int) -> Filter:
    """
        Creates a new instance of Filter where the network is empty and the binary outputs are of length n
        
        n must be greater than 1
    """
    return Filter(Network.emptyNetwork(), Network.allOutputs(Network.emptyNetwork(), n))

def net(f: Filter) -> Network.Network:
    """
        Returns the network in filter f
    """
    return f.netw

def out(f: Filter) -> list[list[int]]:
    """
        Returns the binary outputs of filter f
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
        Returns true if the comparator c is redundant according to f
        Returns false if not
        i.e. returns true if the length of the binary outputs of f doesn't change if c is applied to it
    """
    return len(out(f)) == len(Network.outputs(tempNet(c), out(f)))

def add(c: Comparator.Comparator, f: Filter) -> Filter:
    """
        Updates filter f by adding comparator c
        i.e. adds a comparator c to the network in f and updates binaryOut in f to reflect this change

        maxChannel of the comparator c must be less than the length of each element in f.binaryOut
    """
    Network.append(c, net(f))
    f.binaryOut = Network.outputs(tempNet(c), out(f))
    return f


def isSorting(f: Filter) -> bool:
    """
        Returns true if the network sorts each binary input and false if not
        Uses the fact that there are n + 1 more lists in a sorted list of lists with n being the amount of element in the inner lists
    """
    return len(out(f)) == len(out(f)[0]) + 1
