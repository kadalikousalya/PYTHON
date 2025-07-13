class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        bitsLeft = lambda x: n - x.bit_length()
        bitsRght = lambda x: (x & -x).bit_length() - 1
         
        sumTwo = firstPlayer + secondPlayer
        difTwo = secondPlayer - firstPlayer

                    # We reset best to more optimal positions if needed
        if sumTwo > n + 1: 
            firstPlayer, secondPlayer = -secondPlayer %(n+1), -firstPlayer %(n+1)
            sumTwo = -sumTwo %(n+1)

                   # We determine the the first element of the solution
                   # based on five possibilities
        if sumTwo == n + 1:             # <-- 1)
            return [1, 1]

        elif sumTwo == n:               # <-- 2)
            if firstPlayer % 2 == 0:
                if  difTwo > 2: early = 2
                else: early = bitsRght(firstPlayer) + 1
            else: early = 1    

        elif difTwo == 1:               # <-- 3)
            early = n - bitsLeft((n - 1) // (sumTwo - 1))
            early += bitsRght((n - 1) >> early)

        elif sumTwo <= (n + 1) // 2:    # <-- 4)  
            early = n - bitsLeft((n - 1) // (sumTwo - 1))

        else: early = 1                 # <-- 5)

                    # We determine the the second element of the solution
        later = n - max(bitsLeft(n - 1), secondPlayer - 1)

        return [early + 1, later]
        