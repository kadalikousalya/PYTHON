class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        z = Counter()
        for p in product((v%k for v in nums),range(k)):
            z[p] = z[p[::-1]]+1

        return max(z.values())
        
