from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split Dataset Into Training And Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Decision Tree classifier
clf = DecisionTreeClassifier()

# Train Decision Tree classifier
clf.fit(X_train, y_train)

# Predict On Test Data
y_pred = clf.predict(X_test)

# Evaluate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy : ", accuracy)
