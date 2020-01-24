import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColorma

data = pd.read_csv("apples_and_oranges.csv")
training_set, test_set = train_test_split(data, test_size = 0.2, random_state = 1)

X_train = training_set.iloc[:,0:2].values
Y_train = training_set.iloc[:,2].values
X_test = test_set.iloc[:,0:2].values
Y_test = test_set.iloc[:,2].values


classifier = SVC(kernel='rbf', random_state = 1)
classifier.fit(X_train,Y_train)


Y_pred = classifier.predict(X_test)
test_set["Predictions"] = Y_pred


cm = confusion_matrix(Y_test,Y_pred)
accuracy = float(cm.diagonal().sum())/len(Y_test)
print("\nAccuracy Of SVM For The Given Dataset : ", accuracy)

le = LabelEncoder()
Y_train = le.fit_transform(Y_train)
