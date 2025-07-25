class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # hash_set=set()
        # max_sum=float('-inf')
        # curr_sum=0
        # i=0
        # j=0  
        # while j<len(nums):
        #     if nums[j] in hash_set:
        #         while nums[j] in hash_set:
        #             hash_set.remove(nums[i])
        #             curr_sum-=nums[i]
        #             i+=1
        #     hash_set.add(nums[j])
        #     curr_sum+=nums[j]
        #     max_sum=max(max_sum,curr_sum)
        #     j+=1
        # if curr_sum<0:
        #     hash_set.clear()
        #     curr_sum=0
        #     i=j

        # return max_sum
        
        s=0
        for i in set(nums) :
            if i >0:
                s+=i
        if s==0:
            return max(nums)
        return s
        