class Solution:
    def possibleStringCount(self, word: str) -> int:
        count=len(word)
        for i in range(1,len(word)):
            if word[i]!=word[i-1]:
                count-=1
        return count
        