class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BRUTE FORCE: O(m * n)
        # loop thru an array incrementing to max num in piles 1 to n
            # loop divide each pile[i] % n until theres nothing left and track count.
            # track min count

        # OPTIMAL: O(nlogm)
        # replace the outer loop with binary search
        # 1 2 3 4

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            hours = 0
            for banana in piles:
                hours += math.ceil(banana / k)

            if (hours <= h):
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
            
        return res

