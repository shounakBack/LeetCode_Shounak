from heapq import *
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def helper(adj,src):
            q=[]
            heappush(q,(0,src))
            d=[math.inf]*(len(adj)+1)
            d[src]=0
            while q:
                dist,node=heappop(q)
                if node==n-1:
                    return dist
                for neigh in adj[node]:
                    if dist+1<=d[neigh]:
                        d[neigh]=d[node]+1
                        heappush(q,(d[node]+1,neigh))
        graph=defaultdict(list)
        out=[]
        for i in range(n):
            if i+1==n:
                break
            graph[i].append(i+1)
        for u,v in queries:
            graph[u].append(v)
            res=helper(graph,0)
            out.append(res)
        return out
                