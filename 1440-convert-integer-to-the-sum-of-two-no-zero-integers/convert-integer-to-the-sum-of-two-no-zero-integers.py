class Solution:
    def isNoZero(self,num):
        while num>0:
            if num%10==0:
                return False
            num=num//10
        return True
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n):
            b=n-a
            if self.isNoZero(a) and self.isNoZero(b):
                return [a,b]

        