class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt=0
        streak=0
        for i in range(len(nums)):
            if nums[i]==0:
                cnt+=1
                streak+=cnt
            else:
                cnt=0
        return streak
        