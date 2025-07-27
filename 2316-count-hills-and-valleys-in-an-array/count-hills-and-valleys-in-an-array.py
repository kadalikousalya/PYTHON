class Solution:
    def countHillValley(self, num: List[int]) -> int:

        res=0
        nums=[num[0]]
        for i in range(1,len(num)):
            if num[i-1]!=num[i]:
                nums.append(num[i])
    
            
        for i in range(1,len(nums)-1):
            if (nums[i]>nums[i+1] and nums[i]>nums[i-1]) or (nums[i]<nums[i+1] and nums[i]<nums[i-1]):
                res+=1
        return res      