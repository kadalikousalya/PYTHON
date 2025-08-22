class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        minRow=float('inf')
        maxRow=float('-inf')
        minCol=float('inf')
        maxCol=float('-inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    minRow=min(minRow,i)
                    maxRow=max(maxRow,i)
                    minCol=min(minCol,j)
                    maxCol=max(maxCol,j)
        height=maxRow-minRow+1
        width=maxCol-minCol+1
        return height*width
        