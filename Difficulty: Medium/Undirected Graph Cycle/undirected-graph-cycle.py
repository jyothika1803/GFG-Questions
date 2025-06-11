class Solution:
	def isCycle(self, V, edges):
		#Code here
		adjacency_list=[]
		for _ in range(V):
		    adjacency_list.append([])
		for u,v in edges:
		    adjacency_list[u].append(v)
		    adjacency_list[v].append(u)
		visited=[False]*V
		def dfs(curr,parent):
		    visited[curr]=True
		    for adjNode in adjacency_list[curr]:
		        if not visited[adjNode]:
		            if dfs(adjNode,curr):
		                return True
		        elif adjNode != parent:
		            return True
		    return False
		for i in range(V):
		    if not visited[i]:
		        if dfs(i,-1):
		            return True
		return False
		