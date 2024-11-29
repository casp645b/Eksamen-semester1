import network
import filter as filt
import generate
import prune

def network_finder(n: int) -> network.Network:
    """
        Finds a sortingnetwork for n channels/inputs

        n must be greater than 1

        >>> netw = network_finder(4)
        >>> network.is_sorting(netw, 4)
        True
    """
    
    filters = [filt.make_empty_filter(n)]

    sortingNetw = []
    while sortingNetw == []:
        filters = generate.extend(filters, n)
        filters = prune.prune(filters, n)
        
        sortingNetw = list(filter(filt.is_sorting, filters))
    return filt.net(sortingNetw[0])
    
    
    filters = [filt.make_empty_filter(n)]
    
    while not filt.is_sorting(filters[0]):
        filters = generate.extend(filters, n)
        filters = prune.prune(filters, n)
    return filt.net(filters[0])

    
    
    
    
def interface() -> None:
    """
        Prints the implementation of a found sortingnetwork that sorts a list v
        with length specified by the input from the user

        The number given in the input function must be an integer greater than 1
    """
    size = int(input("How many inputs should the network sort? "))

    sortingNetwork = network_finder(size)
    print("The found sortingnetwork on " + str(size) + " channels consists of " +
          str(network.size(sortingNetwork)) + " comparators.")
    toWrite = network.to_program(sortingNetwork, "v", "")
    print("The Python implementation for sorting a list v of size " + str(size) + " is:")
    for i in toWrite:
        print(i)



if __name__ == "__main__":
    interface()


