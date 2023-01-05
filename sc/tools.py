from scanpy import AnnData
def subset(adata:AnnData,subsets:dict,inplace:bool=True) -> AnnData:
    """
    对adata取子集
    """
    _adata = adata if inplace else adata.copy()
    for k in subsets.keys():
      #  adata = adata[adata.obs[k].isin([subsets.get(k)]),:]
      _adata = _adata[_adata.obs[k].apply(lambda x: eval(subsets.get(k))), :]

    return None if inplace else _adata