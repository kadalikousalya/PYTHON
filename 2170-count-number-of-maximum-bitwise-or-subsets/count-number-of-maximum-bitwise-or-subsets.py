class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        max_or=0
        count=0
        for mask in range(1,1<<n):
            subset_or=0
            for i in range(0,n):
                if mask&(1<<i):
                    subset_or |=nums[i]
            if subset_or>max_or:
                max_or=subset_or
                count=1
            elif subset_or==max_or:
                count+=1
        return count
