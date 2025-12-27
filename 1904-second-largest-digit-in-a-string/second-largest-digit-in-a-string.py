class Solution:
    def secondHighest(self, s: str) -> int:
        larg=-1
        sec_lar=-1
        for ch in s:
            if ch  in '0123456789':
                ch1=int(ch)
                if ch1>larg:
                    sec_lar=larg
                    larg=ch1
                elif ch1<larg and ch1>sec_lar:
                    sec_lar=ch1
        return sec_lar


        