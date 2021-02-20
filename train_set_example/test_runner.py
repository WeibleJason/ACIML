from load import load_csv
from binary_tree import BinaryTree
from binary_node import BinaryNode
import numpy as np

data = load_csv('A Course in Machine Learning - Training Set - Sheet1.csv')
data = np.asarray(data) # convert string matrix to ndarray
data = np.delete(data,0,0) # remove first row with category labels
data_arr = np.ndarray.flatten(data) # flatten matrix into array


tree = BinaryNode()
rootNode = BinaryTree.createLevelOrder(data_arr,tree,0,45)
# BinaryTree.inOrderPrint(rootNode)
# print(data_arr)
rootNode.printVisualTree()
print()



