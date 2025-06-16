class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i=0
        j=0
        max_diff=-1
        while j<len(nums):
            if nums[i]<nums[j]:
                max_diff=max(max_diff,nums[j]-nums[i])
            else:
                i=j
            j+=1
        return max_diff
