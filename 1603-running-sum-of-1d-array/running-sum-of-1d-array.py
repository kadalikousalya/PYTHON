class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            result.append(s)
        return result

        