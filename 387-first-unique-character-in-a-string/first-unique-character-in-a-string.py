class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for num in range(len(s)):
            if freq[s[num]]==1:
                return num
        return -1
        