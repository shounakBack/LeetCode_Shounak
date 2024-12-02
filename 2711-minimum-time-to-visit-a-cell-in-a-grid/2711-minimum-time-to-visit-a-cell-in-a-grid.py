class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        q=[]
        travel=[(0,1),(1,0),(0,-1),(-1,0)]
        heappush(q,(grid[0][0],0,0))
        visited=set()
        row,col=len(grid),len(grid[0])
        while q:
            time,r,c=heappop(q)
            if r==row-1 and c==col-1:
                return time
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for dx,dy in travel:
                nx,ny=dx+r,dy+c
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited:
                    diff=grid[nx][ny]-time
                    if diff%2==0:
                        waste=1
                    else:
                        waste=0
                    t=max(grid[nx][ny]+waste,time+1)
                    heappush(q,(t,nx,ny))
        return -1