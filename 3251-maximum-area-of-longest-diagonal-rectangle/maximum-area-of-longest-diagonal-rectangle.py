class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n=len(dimensions)
        max_diag=-1
        max_area=-1
        for i in range(n):
            l=dimensions[i][0]
            w=dimensions[i][1]
            diag=(l*l)+(w*w)
            area=l*w
            if(diag>max_diag):
                max_diag=diag
                max_area=area
            elif(diag==max_diag):
                max_area=max(max_area,area)
        return max_area


        