from collections import deque

class Solution:
    def topoSort(self, V, edges):
        # Finding the indegree of every node
        indegree = [0] * V

        # Creating the adjacency list
        adj_list = [[] for _ in range(V)]

        for u, v in edges:
            adj_list[u].append(v)

        # Iterating over the adjacency list to find indegree
        for i in range(V):
            for adj_node in adj_list[i]:
                indegree[adj_node] += 1

        queue = deque()
        # Add all the nodes having indegree 0 to the queue
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        ans = []

        # Continuing the BFS
        while queue:
            curr = queue.popleft()
            ans.append(curr)

            # Reducing the indegree of all adjacent nodes
            for adj_node in adj_list[curr]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        return ans

