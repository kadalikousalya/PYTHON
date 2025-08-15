class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>0:
            if n==1:
                return True
            elif n<1:
                return False
            else:
                n=n/4
        return False

        

        