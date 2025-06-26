from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        v=len(adj)
        visited=[False]*v
        ans=[]
        queue=deque()
        src=0
        visited[src]=True
        queue.append(src)
        while queue:
            curr=queue.popleft()
            ans.append(curr)
            for x in adj[curr]:
                if not visited[x]:
                    visited[x]=True
                    queue.append(x)
        return ans