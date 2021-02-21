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


def iOPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        if node is not None:
            node.PrintTree()
            node.left.PrintTree()
            node.right.PrintTree()


data = load_csv('A Course in Machine Learning - Training Set - Sheet1.csv')
data = np.asarray(data) # convert string matrix to ndarray
feature_names = data[0,:] # extract feature names
examples = np.delete(data,0,0) # remove first row with feature names
# create dict of feature to example values
feature_dict = {}
i = 0
while i < len(feature_names):
    feature_dict.update({feature_names[i]:examples[:,i]})
    i = i + 1

# Create decision tree
root = DTTrain(examples,feature_dict)
iOPrint(root)


