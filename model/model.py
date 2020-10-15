#import library
import pickle
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
np.random.seed(42)

#load data
data_set=pd.read_csv("model/data.csv")

#load sample data
#print (data_set.head())

#handle miising data
#print(data_set.info())

drop_data=data_set.drop(["Unnamed: 32", "id"], axis=1, inplace =True)     #remove the uunamed column and 

#print(data_set.head()) #show data

#sns.heatmap(data_set.corr()) #show shape data
#plt.show()

#map labled data to number
data_set["diagnosis"]=data_set["diagnosis"].map({"M":0,"B":1})
print(data_set.head()) #show data

x=data_set.drop('diagnosis',axis=1)
y=data_set['diagnosis']

#split data to train/ test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#choose model 
model =svm.SVC(kernel="linear", C=1 , gamma=1)

#train model 
model.fit(x_train,y_train)


#tunne model prams
#from sklearn.model_selection import GridSearchCV
#prams={"kernel":("linear","rbf"), "C":[1,5,10], "gamma":[1,0.1,0.01,0.001]}
#grid=GridSearchCV(svm.SVC(),prams,verbose=0)
#grid.fit(x_train,y_train)

#validate modle

print(model.score(x_train,y_train)) #output 0.9692307692307692
print(model.score(x_test,y_test))  #output 0.956140350877193

#save model 
pickle.dump(model , open(r"breast_cancer.pkl","wb"))

