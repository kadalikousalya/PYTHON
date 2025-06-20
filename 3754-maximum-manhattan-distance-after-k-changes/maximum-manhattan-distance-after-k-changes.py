class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n=s1=w=e=0
        ans=0
        for i in range(len(s)):
            if s[i]=='S':
                s1+=1
            elif  s[i]=='N':
                n+=1
            elif s[i]=='E':
                e+=1
            elif s[i]=="W":
                w+=1
            x=abs(e-w)
            y=abs(n-s1)

            md=x+y
            steps=i+1
            extra=min(2*k,steps-md)
            dis=md+extra
            ans=max(ans,dis)
        return ans

              
        