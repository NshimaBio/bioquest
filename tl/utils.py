import itertools

# def flatten(nest_list):
#     nl = nest_list.copy()
#     import itertools
#     for x,y in enumerate(nl):
#         if not isinstance(y, list):
#             nl[x] = [y]
#     return list(itertools.chain.from_iterable(nl))

flatten = lambda nest_list: sum(([x] if not isinstance(x, list) else flatten(x) for x in nest_list), [])