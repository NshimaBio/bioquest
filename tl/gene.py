import numpy as np
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

def deg_siglabel(
        df: pd.DataFrame, 
        lfc='LogFC',
        padj:str = None,
        pvalue:str = None,
        lfc_thr=(.585, .585),
        pv_thr=(0.05, 0.05),
        siglabel=('Significant down', 'Not significant', 'Significant up')
        ) -> pd.DataFrame:
    """
    label genes for significant up/down or not significant
    lfc
    pv
    padj
    """
    pv = pvalue if pvalue else padj
    # upregulated
    lg_up = np.logical_and(df[lfc] >= lfc_thr[1],df[pv] < pv_thr[1])
    df.loc[lg_up,'Change'] = siglabel[2]
    # downregulated
    lg_down = np.logical_and(df[lfc] <= -lfc_thr[0],df[pv] < pv_thr[0])
    df.loc[lg_down, 'Change'] = siglabel[0]
    df.fillna(value={'Change': siglabel[1]}, inplace=True)
    # return df
    print(f'All degs: {df.loc[df.Change != siglabel[1], :].shape[0]}')
    print(
        f'Significant up: {df.loc[df.Change == siglabel[2],:].shape[0]}')
    print(
        f'Significant down: {df.loc[df.Change == siglabel[0],:].shape[0]}')
    return df


def deg_filter(
        frame: pd.DataFrame,
        lfc :str='LogFC',
        top_n=None,
        filter_label=['Significant up','Significant down']
        ) -> pd.DataFrame:
    if top_n:
        _df = frame.sort_values(by=lfc)
        nrow = frame.shape[0]
        dfslice = list(range(0, top_n)) + \
            list(range(nrow-top_n, nrow))
        return _df.iloc[dfslice, :]
    else:
        return bq.tl.subset(frame,{"Change":filter_label})
