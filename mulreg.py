import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv("housing.csv")
dataset.isnull().sum()

pd.plotting.scatter_matrix(dataset)

plt.scatter(dataset['housing_median_age'], dataset["median_house_value"])
plt.show()

X = dataset.iloc[:,[0,1,2,3,4,5,6,7,9]].values
X=pd.DataFrame(X)
y = dataset.iloc[:,8].values


from sklearn.preprocessing import Imputer
im = Imputer(strategy = "median")
X[:,[4]] = imp.fit_transform(X[:,[4]])


corr_mat = dataset.corr()
import seaborn as sns
sns.heatmap(corr_mat, annot = True)

X = dataset.iloc[:,[0,1,2,3,4,5,6,7,9]].values
X=pd.DataFrame(X)
y = dataset.iloc[:,8].values
y=pd.DataFrame(y)

