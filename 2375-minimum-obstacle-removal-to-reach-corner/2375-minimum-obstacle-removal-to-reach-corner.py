from heapq import *
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q=[]
        travel=[(0,1),(1,0),(0,-1),(-1,0)]
        heappush(q,(grid[0][0],0,0))
        visited=set()
        visited.add((0,0))
        row,col=len(grid),len(grid[0])
        while q:
            obstacle,r,c=heappop(q)
            if r==row-1 and c==col-1:
                return obstacle
            for dx,dy in travel:
                nx,ny=dx+r,dy+c
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    heappush(q,(obstacle+grid[nx][ny],nx,ny))
            