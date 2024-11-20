import network
import filter
import generate
import prune

def network_finder(n: int) -> network.Network:
    """
        Finds a sortingnetwork for n channels/inputs
    """
    filters = [filter.make_empty_filter(n)]
    while not filter.is_sorting(filters[0]):
        filters = generate.extend(filters, n)
        filters = prune.prune(filters, n)
    return filter.net(filters[0])
