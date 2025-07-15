class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel_count=0
        const_count=0
        for i in range(len(word)):
            if word[i].isalpha():
                if word[i] in ['a','e','i','o','u','A','E','I','O','U']:
                    vowel_count+=1
                else:
                    const_count+=1
            elif not word[i].isdigit():
                return False
        return vowel_count>=1 and const_count>=1



        