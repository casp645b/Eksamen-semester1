from dataclasses import dataclass
import comparator
import functools

@dataclass
class Network:
    """
        Class that contains a list of comparators to use
    """
    comparators: list[comparator.Comparator]


def empty_network() -> Network:
    """
        Creates a new empty instance of network

        >>> empty_network()
        Network(comparators=[])
    """
    return Network([])


def append(c: comparator.Comparator, net: Network) -> Network:
    """
        Adds a comparator to the end of the network

        >>> append(comparator.make_comparator(0, 1), empty_network())
        Network(comparators=[Comparator(channel1=0, channel2=1)])
    """
    newNet = Network(net.comparators.copy())
    newNet.comparators.append(c)
    return newNet

def size(net: Network) -> int:
    """
        Returns the number of comparators in the network

        >>> size(append(comparator.make_comparator(0, 1), empty_network()))
        1
    """
    return len(net.comparators)

def max_channel(net: Network) -> int:
    """
        Returns the largest channel the network can affect

        Function cannot take empty networks

        >>> max_channel(append(comparator.make_comparator(0, 1), empty_network()))
        1
    """
    return max(map(comparator.max_channel, net.comparators))


def is_standard(net: Network) -> bool:
    """
        Returns true if all comparators in the network are "Standard"
        else returns false

        >>> is_standard(append(comparator.make_comparator(0, 1), empty_network()))
        True
    """
    return list(filter(comparator.is_standard, net.comparators)) == net.comparators


def apply(net: Network, w: list[int]) -> list[int]:
    """
        Applies the comparators in a network to the list w

         the length of w has to greater than max_channel of net
        >>> apply(append(comparator.make_comparator(0, 1), empty_network()), [3, 2, 1])
        [2, 3, 1]
    """
    return list(functools.reduce(lambda x, y: comparator.apply(y, x),
                                 net.comparators, w))


def outputs(net: Network, w: list[list[int]]) -> list[list[int]]:
    """
        Returns a list of unique lists (i.e. removes duplicates)
        as a result of net being applied to the lists in w

        the length of each element of w must be greater than max_channel of net

        >>> outputs(append(comparator.make_comparator(0, 1),
        ... empty_network()), [[3, 2, 1], [2, 3, 1], [2, 1, 3]])
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


def all_outputs(net: Network, n: int) -> list[list[int]]:
    """
        Returns the output of the outputs function
        for all binary permutations of a list with length n

        n has to be greater than max_channel of net

        >>> all_outputs(append(comparator.make_comparator(0, 1), empty_network()), 3)
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]
    """
    v = list(map(lambda x: base_ten_to_binary(x, n), range(2**n)))
    return outputs(net, v)


def base_ten_to_binary(m: int, n: int) -> list[int]:
    """
        Converts a base ten number m to a list reprecenting its binary value
        of length n
        Purpose is to help allOutputs function
        
        m must be less than 2^n
        
        >>> base_ten_to_binary(29, 7)
        [0, 0, 1, 1, 1, 0, 1]
    """
    v = list(map(lambda x: pow(2, x), range(n-1, -1, -1)))
    return list(map(lambda x: (m//v[x])%2, range(n)))


def is_sorting(net: Network, size: int) -> bool:
    """
        Check whether or not the comparator network net 
        is a sorting network to size inputs,
        i.e. check whether or not net will correctly sort all lists of length size
        

        
        size must be greater than the maximum channel the network refers to 
        for this function to be used

        >>> is_sorting(append(comparator.make_comparator(0, 1), empty_network()), 3)
        False

        >>> is_sorting(append(comparator.make_comparator(0, 1), empty_network()), 2)
        True
    """
    return len(all_outputs(net, size)) == size + 1


def to_program(net: Network, var: str, aux: str) -> list[str]:
    """
        Returns a list of strings that, if inserted in  Python shell,
        sorts a list with name var based on instructions in network

        Does not use the variable aux

        >>> to_program(append(comparator.make_comparator(0, 1), empty_network()),
        ... "a", "b")
        ['i = 0', 'j = 1', 'if a[i] > a[j]:', '  a[i], a[j] = a[j], a[i]']

        >>> to_program(append(comparator.make_comparator(1, 2),
        ... append(comparator.make_comparator(0, 1), empty_network())), "a", "b")
        ['i = 0', 'j = 1', 'if a[i] > a[j]:', '  a[i], a[j] = a[j], a[i]', \
'i = 1', 'j = 2', 'if a[i] > a[j]:', '  a[i], a[j] = a[j], a[i]']
    """
    return list(functools.reduce(lambda x, y: x+y,
                                 map(lambda x: comparator.to_program(x, var, aux),
                                     net.comparators), []))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
