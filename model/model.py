from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt 
import pickle

data=load_wine()

X=data.data
y=data.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.8,random_state=1)

classifier_knn = KNeighborsClassifier(n_neighbors = 3)
classifier_knn.fit(X_train, y_train)
y_pred = classifier_knn.predict(X_test)

pickle.dump(classifier_knn,open('model.pkl','wb'))

print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
