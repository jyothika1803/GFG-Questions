"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
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
            result.append(level_nodes)
            level+=1
        return result