class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        count=1
        nums.sort()
        min_value=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-min_value>k:
                min_value=nums[i]
                count+=1
        return count

        