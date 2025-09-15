class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split(" ")
        brokenLetters=set(brokenLetters)
        res=0
        for i in text:
            for j in range(len(i)):
                if i[j] in brokenLetters:
                    break
            else:
                res+=1
        return res
        
        
        