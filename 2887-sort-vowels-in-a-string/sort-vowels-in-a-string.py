class Solution:
    def sortVowels(self, s: str) -> str:
        sorted_list=[]
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O',"U"]:
                sorted_list.append(i)
        sorted_list.sort()
        res=[]
        k=0
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O',"U"]:
                res.append(sorted_list[k])
                k+=1
            else:
                res.append(i)
        return "".join(res)

        
        