from binary_node import BinaryNode

class BinaryTree:
    '''
    A binary tree
    :returns object whose root contains an empty Binary Node
    '''
    left_index_set1 = set()
    right_index_set1 = set()
    left_index_set2 = set()
    right_index_set2 = set()
    height = 0

    def __init__(self):
        self.root = BinaryNode()

    def print(func):
        '''
        prints the output of
        :param func()
        '''
        # print(func())


    def createLevelOrder(array,root,index,indent):
        '''
        creates a binary tree in level order of the given array
        :param array - the array of data
        :param index = initial index of array, should be 0 to get entire array
        :returns the root node of the binary tree
        '''
        length = len(array)
        if index < length:
            root = BinaryNode()
            root.data = array[index]
    
                    
            
            root.left = BinaryTree.createLevelOrder(array,root.left, 2 * index + 1,indent)
            root.right = BinaryTree.createLevelOrder(array,root.right, 2 * index + 2,indent)

        return root
            


    def inOrderPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        if node is not None:
            BinaryTree.inOrderPrint(node.left)
            print("Name: " + node.data + " Data: " + node.data)
            BinaryTree.inOrderPrint(node.right)

    def inOrderDataTraverse(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        value = None
        if node is not None:
            BinaryTree.inOrderPrint(node.left)
            value = node.data
            BinaryTree.inOrderPrint(node.right)
        return value

    
    def preOrderPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        if node is not None:
            print("Name: " + node.data + " Data: " + node.data)
            BinaryTree.inOrderPrint(node.left)
            BinaryTree.inOrderPrint(node.right)


    def postOrderPrint(node):
        '''
        print a tree in order
        :param node is the root of the tree
        '''
        if node is not None:
            BinarTree.inOrderPrint(node.left)
            BinaryTree.inOrderPrint(node.right)
            print("Name: " + node.data + " Data: " + node.data)

    
    def treeToArray(node,array):
        if node is not None:
            
            temp_array = BinaryTree.treeToArray(node.left,array)
            if temp_array is not None:
                array = temp_array

            array.append(node.data)

            temp_array = BinaryTree.treeToArray(node.right,array)
            if temp_array is not None:
                array = temp_array

        return array


    def InOrderTraverse(traverse_array,array,index):

        length = len(array)
        
        if index < length:
            
            traverse_array = BinaryTree.InOrderTraverse(traverse_array,array, 2 * index + 1)
            traverse_array.append(array[index])
            traverse_array = BinaryTree.InOrderTraverse(traverse_array,array, 2 * index + 2)

        return traverse_array



    def createIndexSet():
        while 2*BinaryTree.height-1 < 1000:
            BinaryTree.left_index_set1.add(2*BinaryTree.height + 1)
            BinaryTree.right_index_set1.add(2*BinaryTree.height + 2)
            BinaryTree.left_index_set2.add(2**BinaryTree.height - 1)
            BinaryTree.right_index_set2.add(2**BinaryTree.height)
            BinaryTree.height = BinaryTree.height + 1
            




