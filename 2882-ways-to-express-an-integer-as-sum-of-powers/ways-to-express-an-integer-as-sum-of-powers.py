class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7  # Large prime for modulo
        
        # Step 1: Generate all x-th powers <= n
        powers = []
        base = 1
        while base ** x <= n:
            powers.append(base ** x)
            base += 1
        # Example: n=10, x=2 -> powers = [1, 4, 9]
        
        # Step 2: Initialize DP array
        # dp[s] = number of ways to make sum 's'
        dp = [0] * (n + 1)
        dp[0] = 1  # One way to make sum 0: pick nothing
        
        # Step 3: Process each power
        for p in powers:
            # Go backwards to ensure we don't reuse the same number twice
            for s in range(n, p - 1, -1):
                # Add ways to make 's - p' into ways to make 's'
                dp[s] = (dp[s] + dp[s - p]) % MOD
        
        # Step 4: Result is ways to make sum n
        return dp[n]
        