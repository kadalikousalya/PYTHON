class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count=[0]*(n+1)
        for num in nums:
            count[num]+=1
        res=[]
        for i in range(1,n+1):
            if count[i]==0:
                res.append(i)
            elif count[i]==2:
                res.insert(0,i)
        return res                

        
        
        