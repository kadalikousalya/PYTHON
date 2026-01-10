from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n,m=len(grid),len(grid[0])
        if not grid or not grid[0]:
            return -1
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=[[[False]*(k+1) for _ in range(m)] for _ in range(n)]
        queue=deque()
        queue.append((0,0,0,0))
        visited[0][0][0]=True
        if grid[0][0]==1 and grid[n-1][m-1]==1:
            return -1
        while queue:
            r,c,steps,used_wall=queue.popleft()
            if r==n-1 and c==m-1:
                return steps
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m:
                    nxt_used=used_wall+grid[nr][nc]
                    if nxt_used<=k and not visited[nr][nc][nxt_used]:
                        visited[nr][nc][nxt_used]=True
                        queue.append((nr,nc,steps+1,nxt_used))
        return -1
            
        