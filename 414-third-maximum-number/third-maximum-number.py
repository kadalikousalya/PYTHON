class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set()
        l=[]
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                l.append(nums[i])

        l.sort(reverse=True)
        if len(l)>=3:
            return l[2]
        else:
            return l[0]



        