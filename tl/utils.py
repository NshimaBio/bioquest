import itertools


# flatten a nest list
# flatten = lambda nest_list: sum(([x] if not isinstance(x, list) else flatten(x) for x in nest_list), [])

def dict_slice(adict:dict, start:int, end:int)->dict:
    '''
    slice a dict using numeric index
    '''
    keys = adict.keys()
    dict_slice = {}
    for k in list(keys)[start:end]:
        dict_slice[k] = adict[k]
    return dict_slice

def flatten(nest_list):
    nl = nest_list.copy()
    import itertools
    for x,y in enumerate(nl):
        if not isinstance(y, list):
            nl[x] = [y]
    return list(itertools.chain.from_iterable(nl))