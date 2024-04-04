# Tree Traversals

class TreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    # PreOrder traversal: Current -> Left -> Right
    def preorder(self,node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
               
    # In order traversal: Left -> Current -> Right
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)       
        
    # Post Order traversal: Left -> Right -> Current
    def postorder(self,node):
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

    

class Tree: 
    pass
class BST:
    pass
    
    
    
    
#-------------------------------------------
# Example usage:
# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#
#
#
#
#

# Perform preorder traversal
print("Preorder traversal:")
root.preorder(root)
    


