class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val=max(nums)
        curr_str=0
        max_str=0
        for i in range(len(nums)):
            if nums[i]==max_val:
                curr_str+=1
                max_str=max(max_str,curr_str)
            else:
                curr_str=0      
        return max_str

        
        