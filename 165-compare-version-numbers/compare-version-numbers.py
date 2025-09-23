class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        v11=[int(x) for x in v1]
        v22=[int(x) for x in v2]
        max_len=max(len(v11),len(v22))
        v11 += [0] * (max_len - len(v11))
        v22+= [0] * (max_len - len(v22))
        for a,b in zip(v11,v22):
            if a<b:
                return -1
            elif a>b:
                return 1
        return 0


        