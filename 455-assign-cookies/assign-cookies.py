class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        max_val=0
        s.sort()
        g.sort()
        i=0
        j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                max_val+=1
                i+=1
            j+=1
        return max_val