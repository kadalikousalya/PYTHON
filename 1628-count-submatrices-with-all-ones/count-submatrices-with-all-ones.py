class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        dp=[[0]*m for _ in range(n)]
        for j in range(m):
            dp[0][j]=mat[0][j]
        for i in range(1,n):
            for j in range(m):
                if mat[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+dp[i-1][j]
        res=0
        for i in range(n):
            for j in range(m):
                
                if dp[i][j]>0:
                    min_height=dp[i][j]
                    for k in range(j,-1,-1):
                        min_height=min(min_height,dp[i][k])
                        res+=min_height
        return res
        
