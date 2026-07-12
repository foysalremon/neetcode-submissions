class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for n in store:
            if (n - 1) not in store:
                length = 1
                while (n + length) in store:
                    length += 1
                res = max(res, length)

        return res