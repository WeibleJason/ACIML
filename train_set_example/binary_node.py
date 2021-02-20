class BinaryNode:

    def __init__(self,name=None,data=None):
        self.left = None
        self.right = None
        self.left_indent = ' ' * 45
        self.right_buffer = 45

    
    def printVisualTree(node):
        if node is not None:
            right_indent = ' ' * node.right_buffer
            data_string = str(node.data)
            if(node.right_buffer==-1):
                print(data_string)
            else:
                print(data_string,end="")
            BinaryNode.printVisualTree(node.left)
            BinaryNode.printVisualTree(node.right)

        

