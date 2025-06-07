class Solution:
    def smallestIndex(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i]<10 and arr[i]==i:
                return i
            if self.digits(arr[i])==i:
                return i
        return -1
            
    def digits(self, num: int) -> int:
        s=0
        while num!=0:
            rem=num%10
            s+=rem
            num=num//10
        return s
            