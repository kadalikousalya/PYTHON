class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        hash_set=defaultdict(int)
        res=0
        for i in s:
            hash_set[i]+=1
            if hash_set[i]%2==0:
                res+=2
        for cnt in hash_set.values():
            if cnt%2:
                res+=1
                break

        return res
            
        
        