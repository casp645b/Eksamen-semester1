import network
import filter as filt
import generate
import prune

def network_finder(n: int) -> network.Network:
    """
        Finds a sortingnetwork for n channels/inputs
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

    
    
    
    


size = int(input("What should the size of the network be?"))

sortingNetwork = network_finder(size)
print(sortingNetwork)

print(network.to_program(sortingNetwork, "v", ""))
