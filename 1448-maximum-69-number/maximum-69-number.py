class Solution:
    def maximum69Number (self, num: int) -> int:
        num_s=str(num)
        max_num=num
        for i,ch in enumerate(num_s):
            if ch=='6':
                new_num=num_s[:i]+"9"+num_s[i+1:]

        
                max_num=max(int(max_num),int(new_num))
        return max_num       