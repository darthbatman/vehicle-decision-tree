import random

# transactions per hour, location [ na: 1, sa: 2, aus: 3, eur: 4, afr: 5, asia: 6], value of transactions
# violation [ yes: 1, no: 0]
x = []
y = []

for i in range(0, 10000):
    wheels = random.randint(2, 4)
    length = random.randint(100, 1000)
    height = random.randint(100, 1000)
    width = random.randint(100, 1000)
    vehicle_type = -1
    if wheels == 2:
        vehicle_type = 1
    elif wheels == 3:
        vehicle_type = 2
    elif wheels == 4:
        vehicle_type = 0
    y.append(vehicle_type)
    x.append([wheels, length, height, width])

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5)

from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)
print x_test
print predictions

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)

# visualization

from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()
tree.export_graphviz(my_classifier, out_file=dot_data, feature_names=["wheels", "length", "height", "width"], class_names=["car", "motorcyle", "trike"], filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("visualization.pdf")