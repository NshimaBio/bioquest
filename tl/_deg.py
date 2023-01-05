def deg_filter(
        df, lfc='log2FC', lfc_thr=(.585, .585),
        pv='pvalue',
        pv_thr=(0.05, 0.05),
        siglabel=('significant down', 'not significant', 'significant up')
):
    df.loc[(df[lfc] >= lfc_thr[0]) & (df[pv] < pv_thr[0]),
           'Change'] = siglabel[2]  # upregulated
    # downregulated
    df.loc[(df[lfc] <= -lfc_thr[1]) &
           (df[pv] < pv_thr[1]), 'Change'] = siglabel[0]
    df.fillna(value={'Change': siglabel[1]}, inplace=True)
    sig_df = df.loc[df.Change != siglabel[1], :]
    n_degs = sig_df.shape[0]
    print(f'All degs: {n_degs}')
    print(
        f'significant up: {sig_df.loc[df.Change == siglabel[2],:].shape[0]}')
    print(
        f'significant down: {sig_df.loc[df.Change == siglabel[0],:].shape[0]}')
    return df

def deg_filter2(
	df,
	lfc='log2FC',
	top_n=None,
	siglabel=('significant down', 'not significant', 'significant up'),
	filter_label='significant down'
	):
	sig_df = df.loc[df.Change != siglabel[1], :]
	n_degs = sig_df.shape[0]
	if top_n:
		_df = df.sort_values(by=[lfc])
		dfslice = list(range(0, top_n))+list(range(df.shape[0]-top_n, df.shape[0]))
		return _df.iloc[dfslice, :]
	else:
		return sig_df.loc[df.Change == filter_label,:]