import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from pandas import DataFrame

def clean(
	feature:DataFrame
	,label:DataFrame
	,selected_feature=None
	,method:str="scale"
	) -> dict:

	if selected_feature:
		feature = feature.loc[:,selected_feature]
	feature_name = feature.columns
	intersection = feature.index.intersection(label.index)
	
	if method == "scale":
		feature = preprocessing.StandardScaler().fit_transform(feature.loc[intersection,:])
	if method == "minmax":
		feature = preprocessing.MinMaxScaler(feature_range=(0,0.999999999)).fit_transform(feature.loc[intersection,:])
	label = preprocessing.LabelEncoder().fit_transform(label.loc[intersection,:])
	
	return {"feature":feature,"label":label,"feature_name":feature_name}
