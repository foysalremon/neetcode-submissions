from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        i = 0
        length = len(nums)

        while i < length:
            sub = target - nums[i]
            if sub in seen:
                return [seen[sub], i]
            seen[nums[i]] = i
            i += 1
