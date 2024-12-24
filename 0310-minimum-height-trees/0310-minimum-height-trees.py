class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        degree=[0]*n
        leaves,res=[],[]
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1
        for i in range(n):
            if degree[i]==1:
                leaves.append(i)
        while leaves:
            curr_leaves=leaves
            leaves,res=[],[]
            for i in range(len(curr_leaves)):
                node=curr_leaves[i]
                res.append(node)
                for neigh in adj[node]:
                    degree[neigh]-=1
                    if degree[neigh]==1:
                        leaves.append(neigh)
        return res
        