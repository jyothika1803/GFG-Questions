#User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if root is None:
            return None
        if root.data==n1 or root.data==n2:
            return root
        left_lca=self.lca(root.left,n1,n2)
        right_lca=self.lca(root.right,n1,n2)
        
        if left_lca and right_lca:
            return root
            
        if left_lca:
            return left_lca
        else:
            return right_lca


