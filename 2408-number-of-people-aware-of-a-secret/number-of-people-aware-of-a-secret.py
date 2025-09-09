class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        learned=[0]*(n+1)
        learned[1]=1
        shares=0
        for day in range(2,n+1):
            if day-delay>=1:
                shares+=learned[day-delay]
            if day-forget>=1:
                shares-=learned[day-forget]
            learned[day] = shares % MOD
        
        # sum of people who still know the secret at the end
        total = sum(learned[max(1, n - forget + 1): n + 1]) % MOD
        return total

        