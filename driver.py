from DecisionTree import *
import pandas as pd
from sklearn import model_selection
import random

option_txt = input ("Select a dataset: (1) Iris, (2) Cars: ")
option = int(option_txt)

while option not in {1,2}:
    option_txt = input ("Incorrect input. Select a dataset: (1) Iris, (2) Cars: ")
    option = int(option_txt)

if option == 1:
    header = ['SepalL', 'SepalW', 'PetalL', 'PetalW', 'Class']
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['SepalL','SepalW','PetalL','PetalW','Class'])
else:
    header = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', header=None, names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])

lst = df.values.tolist()
t = build_tree(lst, header)
print_tree(t)

print("********** Leaf nodes ****************")
leaves = getLeafNodes(t)
for leaf in leaves:
    print("id = " + str(leaf.id) + " depth =" + str(leaf.depth))
print("********** Non-leaf nodes ****************")
innerNodes = getInnerNodes(t)
for inner in innerNodes:
    print("id = " + str(inner.id) + " depth =" + str(inner.depth))

trainDF, testDF = model_selection.train_test_split(df, test_size=0.2)
train = trainDF.values.tolist()
test = testDF.values.tolist()

t = build_tree(train, header)
print("*************Tree before pruning*******")
print_tree(t)
acc = computeAccuracy(test, t)
print("Accuracy on test = " + str(acc))

## TODO: You have to decide on a pruning strategy
"t_pruned = prune_tree(t, [26, 11, 5])"
pruneIDs = nodesToPrune(t, [])
"""prune_innerNodes = random.choices(innerNodes, k=)
id =[]
for node in prune_innerNodes:
    id.append(node.id)"""
t_pruned = prune_tree(t, pruneIDs)

print("*************Tree after pruning*******")
print_tree(t_pruned)
acc = computeAccuracy(test, t_pruned)
print("Nodes pruned = " + str(len(pruneIDs)))
print("Accuracy on test = " + str(acc))
