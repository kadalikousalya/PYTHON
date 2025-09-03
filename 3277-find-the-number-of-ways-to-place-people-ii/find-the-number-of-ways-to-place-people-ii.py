class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:(p[0],-p[1]))
        n=len(points)
        count=0
        for i in range(n):
            max_y=float('-inf')
            for j in range(i+1,n):
                if points[j][1]<=points[i][1]:
                    if points[j][1]>max_y:
                        count+=1
                    max_y=max(max_y,points[j][1])
        return count


        