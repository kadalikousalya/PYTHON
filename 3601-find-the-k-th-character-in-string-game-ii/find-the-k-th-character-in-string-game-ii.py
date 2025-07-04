class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lengths=[1]
        for op in operations:
            if op==0:
                lengths.append(lengths[-1]*2)
            else:
                lengths.append(lengths[-1]*2)
        shift_count=0
        indx=len(operations)
        while indx>0:
            op = operations[indx - 1]

            curr_length=lengths[indx]
            previous_length=lengths[indx-1]
            if k>previous_length:
                k-=previous_length
                if op == 1:
                    shift_count += 1
            indx-=1
        final_char = chr((ord('a') - ord('a') + shift_count) % 26 + ord('a'))
        return final_char

