class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1=nums1
        self.n2=nums2
        self.m=Counter(nums2)

        

    def add(self, index: int, val: int) -> None:
        old_val=self.n2[index]
        self.m[old_val]-=1
        self.n2[index]+=val
        self.m[self.n2[index]]+=1



    def count(self, tot: int) -> int:
        c=0
        for i in self.n1:
            c+=self.m[tot-i]
        return c
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)