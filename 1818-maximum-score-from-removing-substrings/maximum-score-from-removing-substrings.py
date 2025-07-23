class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_pairs(pairs,score):
            nonlocal s
            res=0
            stack=[]
            for c in s:
                if c==pairs[1] and stack  and stack[-1]==pairs[0]:
                    stack.pop()
                    res+=score
                else:
                    stack.append(c)
            s="".join(stack)
            return res
        res=0
        pairs="ab" if x>y else "ba"
        res+=remove_pairs(pairs,max(x,y))
        res+=remove_pairs(pairs[::-1],min(x,y))

        return res


        