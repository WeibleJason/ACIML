from binary_node import BinaryNode

class BinaryTree:
    '''
    A binary tree
    :returns object whose root contains an empty Binary Node
    '''

    def __init__(self):
        self.root = BinaryNode()

    def print(func):
        '''
        prints the output of
        :param func()
        '''
        # print(func())


    def createLevelOrder(array):
        '''
        creates a binary tree in level order of the given array
        :param array - the array of data
        :returns the root node of the binary tree
        '''



    def inOrderPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        while node is not Node:
            inOrderPrint(node.left)
            print("Name: " + node.data + "Data: " + node.data)
            inOrderPrint(node.right)

    
    def preOrderPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        while node is not Node:
             print("Name: " + node.data + "Data: " + node.data)
            inOrderPrint(node.left)
            inOrderPrint(node.right)


    def postOrderPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        while node is not Node:
            inOrderPrint(node.left)
            inOrderPrint(node.right)
            print("Name: " + node.data + "Data: " + node.data)




