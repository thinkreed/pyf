def is_reciprocal_link(graph, source, destination, k):
    if k == 0:
        if destination == source:
            return True
        else:
            return False

    if source in graph[destination]:
        return True

    for node in graph[destination]:
        if is_reciprocal_link(graph, source, node, k - 1):
            return True
    return False


def compute_ranks(graph, k):
    d = 0.8  # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciprocal_link(graph, node, page, k):
                        newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


g = {'a': ['a', 'b', 'c'], 'b': ['a'], 'c': ['d'], 'd': ['a']}
print(compute_ranks(g, 0))
print(compute_ranks(g, 1))
print(compute_ranks(g, 2))
