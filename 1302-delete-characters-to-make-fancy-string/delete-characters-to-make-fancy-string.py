class Solution:
    def makeFancyString(self, s: str) -> str:
        new_str=''
        k=0
        s_new=s[0]
        for i in s:
            if i==s_new:
                k+=1
                if k<3:
                    new_str+=i
            elif i!=new_str:
                k=1
                new_str+=i
                s_new=i
        return new_str

        