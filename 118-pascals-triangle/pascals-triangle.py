class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for rows_num in range(numRows):
            rows=[1]*(rows_num+1)
            for j in range(1,rows_num):
                rows[j]=triangle[rows_num-1][j-1]+triangle[rows_num-1][j]
            triangle.append(rows)
        return triangle

        
        