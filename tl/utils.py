import itertools

def flatten(nest_list):
    nl = nest_list.copy()
    for x,y in enumerate(nl):
        if not isinstance(y, list):
            nl.pop(x)
            nl.insert(x,[y])
    return list(itertools.chain.from_iterable(nl))