class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        dict_freq={}
        for char in word:
            if char in dict_freq:
                dict_freq[char]+=1
            else:
                dict_freq[char]=1
        freq_list=list(dict_freq.values())
        n=len(freq_list)
        min_target=float('inf')
        for base in freq_list:
            dlt=0
            for f in freq_list:
                if f<base:
                    dlt+=f
                elif f>base+k:
                    dlt+=f-(base+k)
            min_target=min(min_target,dlt)
        return min_target
    




