class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums)%k==0:
            return 0
        if sum(nums)%k!=0:
            rem=sum(nums)%k
            return rem
        if sum(nums)<k:
            return sum(nums)
        