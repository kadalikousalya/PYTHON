class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x1=abs(x-z)
        y1=abs(z-y)
        if x1<y1:
            return 1
        elif y1<x1:
            return 2
        elif x1==y1:
            return 0
        