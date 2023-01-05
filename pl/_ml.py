import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from sklearn.metrics import RocCurveDisplay
from sklearn.calibration import CalibrationDisplay
from sklearn.preprocessing import MinMaxScaler
from bioquest.pl._pallete import Pallete

def ROC(y_true, y_hat, od=None,suff='') -> Figure:
	"""
	绘制ROC曲线
	y_true: array | DataFrame
	y_hat: DataFrame
	od: output directory
	falg: filename suffix 
	"""
	for i in range(y_hat.shape[1]):
		RocCurveDisplay.from_predictions(y_true, y_hat.iloc[:,i], name = y_hat.columns[i], color= Pallete.set2[i], ax=plt.gca(),linewidth=2)
	plt.plot([0,1],[0,1], linestyle="dashed",color = "grey");
	plt.ylabel("True Positive Rate");
	plt.xlabel("False Positive Rate");
	p = plt.gcf()
	p.set_size_inches(6, 6)
	plt.close()
	if od:
		p.savefig(od + "/ROC"+ suff + ".pdf")
	return p


def CC(y_true, y_hat, od=None,suff='') -> Figure:
	"""
	绘制校准曲线
	y_true: array | DataFrame
	y_hat: DataFrame
	od: output directory
	falg: filename suffix 
	"""
	names = y_hat.columns
	if any(y_hat.min()<0) or any(y_hat.max()>0):
		y = MinMaxScaler((.0000000001,.9999999999)).fit_transform(y_hat)
	else:
		y = y_hat.values
	for i in range(y_hat.shape[1]):
		CalibrationDisplay.from_predictions(y_true, y[:,i], name = names[i], color= Pallete.set2[i], ax=plt.gca(),linewidth=2)
	plt.plot([0,1],[0,1], linestyle="dashed",color = "grey");
	plt.ylabel("True Positive Rate");
	plt.xlabel("False Positive Rate");
	p = plt.gcf()
	p.set_size_inches(6, 6)
	plt.close()
	if od:
		p.savefig(od + "/CalibrationCurve"+ suff + ".pdf",dpi=300)
	return p

def learning_curve(x,xlabel='',ylabel='',mark:int=0, od:str=None) -> Figure :
	plt.rc('axes', labelsize=16) #fontsize of the x and y labels
	plt.rc('xtick', labelsize=12) #fontsize of the x tick labels
	plt.rc('ytick', labelsize=12)
	plt.plot(np.arange(mark, len(x)+mark), 
		x,
		color='grey', 
		linewidth=.8,
		# linestyle='dashed', 
		marker='o',
		markerfacecolor='white',
		markeredgecolor='r',
		markersize=5
		)
	plt.plot(np.where(x==x.max())[0] + mark,
		x.max(),
		marker='o',
		markerfacecolor='white',
		markersize=10,
		markeredgecolor='b'
		)
	plt.gca().spines.right.set_visible(False)
	plt.gca().spines.top.set_visible(False)
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	p = plt.gcf()
	p.set_size_inches(9, 6)
	plt.close()
	if od:
		p.savefig(od + "/LearningCurve"+ ".pdf",dpi=300)
	return p
