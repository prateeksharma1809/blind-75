from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for source,target in edges:
            graph[source].append(target)
            graph[target].append(source)
        
        visit = [False for _ in range(n)]
        def dfs(node):
            visit[node]=True
            for neigh in graph[node]:
                if not visit[neigh]:
                    dfs(neigh)

        ccCount = 0  
        for i in range(n):
            if not visit[i]:
                dfs(i)
                ccCount+=1
        return ccCount