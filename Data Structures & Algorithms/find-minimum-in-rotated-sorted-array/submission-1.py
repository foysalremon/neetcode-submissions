class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            if l != 0 and nums[l] < nums[l - 1]:
                break
            m = (r + l)//2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m

        return nums[l]