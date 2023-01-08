import bioquest as bq
def select(frame,pattern=None,columns=None):
	if pattern:
		cidx = bq.st.detect(string=frame.columns,pattern=pattern)
	if columns:
		cidx = frame.columns.isin(values=columns)
	return frame.loc[:,cidx]