import math


class node:

        def __init__(self, data=None): 
            self.left = None    
            self.right = None
            self.data = data 

            
class BinarySearchTree: 
    
    def __init__(self):
        self.root = None

    def insert(self, data): 
        if self.root is None: 
            self.root = node(data) 
        else:
            self._insert(data, self.root)
 
    def _insert(self, data, cur_node):
            
                    if data < cur_node.data: 
                        if cur_node.left is None: 
                            cur_node.left = node(data) 
                            cur_node.left.parent = cur_node
                        else: 
                                self._insert(data, cur_node.left) 
                    elif data > cur_node.data:
                        if cur_node.right is None: 
                            cur_node.right = node(data) 
                            cur_node.right.parent = cur_node
                        else: 
                            self._insert(data, cur_node.right) 
                            
    def searchkey(self, data):    
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                print(str(is_found) + " is found")
            else:
                print("Not found")
        else:
                print("Not found")
    
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return data
    
    def list_in(self): 
      if self.root:
        traversal = self.inorderTraversal(self.root)
        print(str(traversal))
        
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res    
    
    def list_post(self):
        if self.root:
            traversal = self.postorderTraversal(self.root)
        print(str(traversal))
            
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res
    
    def list_pre(self):
        if self.root:
             traversal = self.preorderTraversal(self.root)
        print(str(traversal))    
        
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res    
    
    def searchkeyDel(self, data):    
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                pass
            else:
                print("key " + str(data) + " does not exist")
        else:
                print("key " + str(data) + " does not exist")
                
    def delete(self, data):
        self.searchkeyDel(data)
        self.deleteNode(self.root, data)
        
    def deleteNode(self, root, data): 
  
        if root is None: 
            return root  
  
        if data < root.data: 
            root.left = self.deleteNode(root.left, data) 
  
        elif(data > root.data): 
            root.right = self.deleteNode(root.right, data) 
  
        if data == root.data: 
          
        # Node with only one child or no child 
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  
              
            elif root.right is None : 
                 temp = root.left  
                 root = None
                 return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
            temp = self.minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
            root.data = temp.data 
  
        # Delete the inorder successor 
            root.right = self.deleteNode(root.right , temp.data)
             
        return root
    
    def minValueNode(node): 
        current = node 
  
    # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left  
  
        return current
    
    def print(self):
        size = self.size(self.root)
        height = self.height(self.root)
        print("the height of T is " + str(height - 1) + " and the size of T is " + str(size))
    
    def size(self, node): 
        if node is None: 
            return 0 
        else: 
            return (self.size(node.left) + 1 + self.size(node.right)) 
        
    def height(self, node): 
        if node is None: 
            return 0 
  
        else : 
        
        # Compute the depth of each subtree 
            lDepth = self.height(node.left) 
            rDepth = self.height(node.right) 
  
        # Use the larger one 
            if (lDepth > rDepth): 
                return lDepth + 1
            else: 
                return rDepth + 1
# Driver program to test the above functions 
# Let us create the following BST 
#      35 
#    /      \ 
#          45 
#   / \    / \ 
#         40
#         /\
#          43
#         /
#        41
#         \
#         42
T = BinarySearchTree()
T.insert(35) 
T.insert(45) 
T.insert(40) 
T.insert(43) 
T.insert(41) 
T.insert(42) 
T.insert(38)
T.delete(30)
T.delete(38)
T.searchkey(38)

T.list_pre()
T.list_in()
T.list_post()

T.print()

# delete(),print() the height of T is 5 and the size of T is 6
  
# Print inoder traversal of the BST 
