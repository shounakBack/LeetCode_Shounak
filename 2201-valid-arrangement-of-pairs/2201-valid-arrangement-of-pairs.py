class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            while adj[node]:
                nextNode = adj[node].popleft()
                dfs(nextNode)
            res.append(node)
        adj=defaultdict(deque)
        start=-1
        indegree,outdegree=defaultdict(int),defaultdict(int)
        res,out=[],[]
        for u,v in pairs:
            adj[u].append(v)
            outdegree[u]+=1
            indegree[v]+=1
        for node in outdegree:
            if outdegree[node]==indegree[node]+1:
                start=node
        if start==-1:
            start=pairs[0][0]
        dfs(start)
        res.reverse()
        for i in range(1,len(res)):
            out.append([res[i-1],res[i]])
        return out