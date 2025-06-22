class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)%k!=0:
            rem=len(s)%k
            padding=k-rem
            s+=fill*padding
        return [s[i:i+k] for i in range(0,len(s),k)]

        