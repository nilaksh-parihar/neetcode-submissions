class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        r = max(piles)
        l = 1
        ans = 0

        while l < r:
            m = (r + l) // 2
            hrs = 0
            for i in piles:
                if hrs > h:
                    break
                hrs += (i + m - 1) // m

            if hrs <= h:
                r = m 
            else:
                l = m + 1

        return l

            