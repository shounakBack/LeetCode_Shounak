class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node,parent):
            nonlocal res
            sub_tree_sum=values[node]
            for child in adj[node]:
                if child!=parent:
                    sub_tree_sum+=dfs(child,node)
            if sub_tree_sum%k==0:
                res+=1
            return sub_tree_sum
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        res=0
        dfs(0,-1)
        return res