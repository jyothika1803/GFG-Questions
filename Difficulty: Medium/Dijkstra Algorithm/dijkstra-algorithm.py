import heapq
from collections import defaultdict

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w)) 
        dist = [float('inf')] * V
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            curr_dist, u = heapq.heappop(heap)
            if curr_dist > dist[u]:
                continue 
            for neighbor, weight in adj[u]:
                if dist[neighbor] > dist[u] + weight:
                    dist[neighbor] = dist[u] + weight
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        return dist

        