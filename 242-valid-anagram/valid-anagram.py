class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq1={}
        freq2={}
        for i in range(len(s)):
            freq1[s[i]]=freq1.get(s[i],0)+1
        for i in range(len(t)):
            freq2[t[i]]=freq2.get(t[i],0)+1
        for ch in freq1:
            if ch not in freq2 or freq1[ch]!=freq2[ch]:
                return False
        return True
        
        

        