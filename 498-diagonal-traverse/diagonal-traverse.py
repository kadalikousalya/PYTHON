class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res=[]
        n=len(mat)
        m=len(mat[0])
        for d in range(n+m-1):
            temp=[]
            for i in range(max(0,d-m+1),min(n-1,d)+1):
                j=d-i
                temp.append(mat[i][j])
            if d%2==0:
                temp=temp[::-1]
            res.extend(temp)
        return res
