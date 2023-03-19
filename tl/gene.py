import pandas as pd
import bioquest as bq

def current_symbol(frame,reference,tax_id=9606):
    '''
    map SYMBOL alias to latest official SYMBOL NAME
    frame: dataframe,index is SYMBOL
    reference: dataframe, can download from ...
    '''
    alias=pd.read_feather(reference)
    alias = bq.tl.subset(alias,{"tax_id":[tax_id]})
    alias=bq.tl.select(alias,columns=["Symbol","Alias"])
    alias.set_index(keys="Symbol",drop=True,inplace=True)
    lg = frame.index.isin(alias.index)
    new = pd.merge(frame.loc[~lg,:],alias,left_index=True,right_on="Alias",how='left')
    
    return pd.concat([new,frame.loc[lg,:]])