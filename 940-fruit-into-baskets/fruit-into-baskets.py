class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        max_count=0
        fruitsCount={}
        for right in range(len(fruits)):
            if fruits[right] in fruitsCount:
                fruitsCount[fruits[right]]+=1
            else:
                fruitsCount[fruits[right]]=1
            
            while len(fruitsCount)>2:
                fruitsCount[fruits[left]]-=1
                if fruitsCount[fruits[left]]==0:
                    del fruitsCount[fruits[left]]
                left+=1
            max_count=max(max_count,right-left+1)
        return max_count



        