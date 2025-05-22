#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        # code here
        if root is None:
            return []
        queue=deque([root])
        result=[]
        level=0
        while queue:
            size=len(queue)
            level_nodes=[]
            for _ in range(size):
                node=queue.popleft()
                level_nodes.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes[0])
            level+=1
        return result