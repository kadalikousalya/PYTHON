class Solution:
    def kthCharacter(self, k: int) -> str:
        s=['a']
        while len(s)<k:
            curr=len(s)
            for i in range(curr):
                next_char=chr(ord('a')+((ord(s[i])-ord('a')+1)%26))
                s.append(next_char)
        return s[k-1]


        