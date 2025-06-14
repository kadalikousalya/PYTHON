class Solution:
    
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            t=0
            while n!=0:
                rem=n%10
                t+=rem*rem
                n=n//10
            return t
        slow=n
        fast=get_next(n)
        while fast!=1 and slow!=fast:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
        return fast==1
    
        


    
         

        