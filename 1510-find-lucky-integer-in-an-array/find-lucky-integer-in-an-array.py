class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        l=[]
        for key,value in freq.items():
            if key==value:
                l.append(key)
        if len(l)==0:
            return -1
        else:
            return max(l)
        