customed Python scripts for Bioinformatics

```python
import bioquest as bq

# parameter string: single string (such as "TCGA-G3-H383-11A")
bq.st.detect(string,pattern,flags)
bq.st.sub(string,pattern,flags)
bq.st.replace(string,pattern,repl,count)
bq.st.remove(string,pattern,flags)
bq.st.count(string,pattern,flags)
bq.st.grep(string,pattern,flags)

# parameter string: a list of strings 
# (such as ["TCGA-G3-H383-11A","TCGA-G3-H383-01A","TCGA-G3-H383-02A"])
bq.st.detects(string,pattern,flags)
bq.st.subs(string,pattern,flags)
bq.st.replaces(string,pattern,repl,count)
bq.st.removes(string,pattern,flags)
bq.st.counts(string,pattern,flags)
bq.st.greps(string,pattern,flags)

# dataframe
bq.tl.select(frame,columns,pattern)
bq.tl.subset(frame,dict)

# export matplotlib figure
bq.tl.export(filename="UMAP", formats=('pdf','png'), od='output', prefix = '', suffix = '', dpi= 300, figsize=(7, 7))

# plot ROC/Calibration curve
bq.pl.ROC(y_true, y_hat, od='.',suff='')
bq.pl.CC(y_true, y_hat, od='.',suff='')
```