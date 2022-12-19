#Write an application using python to stimulate supervised learning model (Logistic Regression)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
dataset=pd.read_csv("diabetes.csv")
print(dataset.head())
print(dataset.shape)
x= dataset.iloc[:,[0,1,2,3,4,5,6,7]].values
y=dataset.iloc[:,[-1]].values
print(x)
print(y)
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2,random_state=0)
sc= StandardScaler()
x_train_new=sc.fit_transform(x_train)
y_test_new=sc.fit_transform(y_test)
print(x_train_new[0:15,:])