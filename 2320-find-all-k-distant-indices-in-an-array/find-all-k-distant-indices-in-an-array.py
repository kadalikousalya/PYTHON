class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        js=[]
        for i in range(len(nums)):
            if nums[i]==key:
                js.append(i)
        l=[]
        for j in js:
            for i in range(len(nums)):
                if abs(i-j)<=k:
                    l.append(i)
        return list(set(l))
