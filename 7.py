#Write an application to simulate supervised Learning
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
dataset=pd.read_csv("iris.csv")
dataset.describe()
x = dataset.iloc[:, [0,1,2,3]].values
y = dataset.iloc[:, 4].values
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x, y,test_size = 0.25,random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
classifier = LogisticRegression(random_state = 0,solver='lbfgs',multi_class = 'auto')
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
print("Accuracy:",accuracy_score(y_test,y_pred))