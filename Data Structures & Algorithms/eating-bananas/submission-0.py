class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def hours_needed(k):
            return sum(((p + k - 1) // k) for p in piles)

        while l < r:
            m = (r + l)//2
            if hours_needed(m) <= h:
                r = m
            else:
                l = m + 1

        return l