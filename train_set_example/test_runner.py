from load import load_csv
from binary_tree import BinaryTree
from binary_node import BinaryNode
from most_frequent import most_frequent as mf
import numpy as np
# https://pypi.org/project/binarytree/
from binarytree import Node 
from binarytree import tree, bst, heap, build
from DecisionTreeTrain import DecisionTreeTrain as DTTrain
from DecisionTreeTrain import Node


feature_dict = {}

def value_is_no(x,test_point):
    values = feature_dict.get(x)
    if values is not None:
        if values[test_point] == 'n' or values[test_point] == '-1' or values[test_point] == '-2':
            return True
        else:
            return False
    else:
        return False


def iOPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        if node is not None:
            node.PrintTree()
            node.left.PrintTree()
            node.right.PrintTree()


def DecisionTreeTest(tree,test_point):
    if (tree.left == None and tree.right == None):
        return tree.data
    elif (tree.left != None or tree.right != None):
        if (value_is_no(tree.data,test_point)):
            return DecisionTreeTest(tree.left,test_point)
        else:
            return DecisionTreeTest(tree.right,test_point)


data = load_csv('A Course in Machine Learning - Training Set - Sheet1.csv')
data = np.asarray(data) # convert string matrix to ndarray
feature_names = data[0,:] # extract feature names
examples = np.delete(data,0,0) # remove first row with feature names
# create dict of feature to example values

i = 0
while i < len(feature_names):
    feature_dict.update({feature_names[i]:examples[:,i]})
    i = i + 1

# Create decision tree
root = DTTrain(examples,feature_dict)
# iOPrint(root)
result = DecisionTreeTest(root,1)




