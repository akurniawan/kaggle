import pandas

from sklearn import model_selection
import tensorflow.contrib.learn.python.learn.estimators as est

data = pandas.read_csv("train.csv")

y, X = train["Survived"], train[["Age", "SibSp", "Fare"]].fillna(0)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)
