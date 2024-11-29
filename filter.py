from dataclasses import dataclass
import comparator
import network

@dataclass
class Filter:
    """
        Dataclass that contains a network of comparators
        as well as all the binary outputs of this network
    """
    netw: network.Network
    binaryOut: list[list[int]]

def make_empty_filter(n: int) -> Filter:
    """
        Creates a new instance of Filter
        where the network is empty and the binary outputs are of the length n
        
        n must be greater than 1

        >>> make_empty_filter(3)
        Filter(netw=Network(comparators=[]), binaryOut=[[0, 0, 0], [0, 0, 1], \
[0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    """
    return Filter(network.empty_network(),
                  network.all_outputs(network.empty_network(), n))

def net(f: Filter) -> network.Network:
    """
        Returns the network in filter f

        >>> net(make_empty_filter(3))
        Network(comparators=[])
    """
    return f.netw

def out(f: Filter) -> list[list[int]]:
    """
        Returns the binary outputs of filter f

        >>> out(make_empty_filter(3))
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], \
[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    """
    return f.binaryOut

def temp_net(c: comparator.Comparator) -> network.Network:
    """
        Returns a network with only one element, namely c

        Used as helping function in multiple functions

        >>> temp_net(comparator.make_comparator(0,1))
        Network(comparators=[Comparator(channel1=0, channel2=1)])
    """
    return network.Network([c])
    

def is_redundant(c: comparator.Comparator, f: Filter) -> bool:
    """
        Returns true if the comparator c is redundant according to f
        Returns false if not
        i.e. returns true if the length of the binary output of f
        doesn't change if c is applied to it

        max_channel of the comparator c
        must be less than the length of each element in f.binaryOut

        >>> filt = make_empty_filter(3)
        >>> comp = comparator.make_comparator(0,1)
        >>> is_redundant(comp, filt)
        False

        >>> filt = add(comp, filt)
        >>> is_redundant(comp, filt)
        True
    """
    return len(out(f)) == len(network.outputs(temp_net(c), out(f)))

def add(c: comparator.Comparator, f: Filter) -> Filter:
    """
        Returns a copy of the filter f, where the comparator c is added
        i.e. makes a new instance of the dataclass Filter that contain a copy
        of the network in the filter f, where the comparator c i added
        and the binary output, that reflects this network

        max_channel of the comparator c
        must be less than the length of each element in f.binaryOut

        >>> filt = make_empty_filter(3)
        >>> comp = comparator.make_comparator(0,1)
        >>> add(comp, filt)
        Filter(netw=Network(comparators=[Comparator(channel1=0, channel2=1)]), \
binaryOut=[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]])
    """

    return Filter(network.append(c, net(f)), 
                  network.outputs(temp_net(c), out(f)))


def is_sorting(f: Filter) -> bool:
    """
        Returns true if the network sorts each binary input and false if not
        Uses the fact that there are n + 1 more lists in a sorted list of lists
        with n being the amount of element in the inner lists

        >>> filt = make_empty_filter(3)
        >>> comp = comparator.make_comparator(0,1)
        >>> filt = add(comp, filt)
        >>> is_sorting(filt)
        False

        >>> filt = make_empty_filter(2)
        >>> comp = comparator.make_comparator(0,1)
        >>> filt = add(comp, filt)
        >>> is_sorting(filt)
        True
    """
    return len(out(f)) == len(out(f)[0]) + 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
