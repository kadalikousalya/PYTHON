from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        n=len(grid)
        m=len(grid[0])
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        directions=[(1,1),(-1,-1),(1,-1),(-1,1),(0,1),(1,0),(-1,0),(0,-1)]
        visited=[[False]*m for _ in range(n)]
        queue=deque()
        queue.append((0,0,1))
        visited[0][0]=True
        while queue:
            r,c,steps=queue.popleft()
            if r==n-1 and c==m-1:
                return steps
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m:
                    if not visited[nr][nc] and grid[nr][nc]==0:
                        visited[nr][nc]=True
                        queue.append((nr,nc,steps+1))
        return -1


        