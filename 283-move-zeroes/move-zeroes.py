class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i=0
        # j=1
        # while j<len(nums):
        #     if nums[i]==0:
        #         if nums[j]!=0:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i+=1
        #         j+=1          
        #     else:
        #         i+=1
        #         j+=1
        # return nums
        left,right=0,1
        while right<len(arr):
            if arr[left]==0:
                if arr[right]!=0:
                    arr[right],arr[left]=arr[left],arr[right]
                    left+=1
                right+=1
            else:
                #arr[left],arr[right+1]=arr[right+1],arr[left]
                left+=1
                right+=1
        return arr
            
        