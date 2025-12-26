class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=0
        temp=x
        while x>0:
            rem=x%10
            res=res*10+rem
            x=x//10
        if res==temp:
            return True
        return False

        