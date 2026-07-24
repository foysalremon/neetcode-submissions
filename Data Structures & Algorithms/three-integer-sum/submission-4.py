class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            if not i == 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                if not j == i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if not k == len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                tsum = nums[i] +  nums[j] + nums[k]
                if tsum > 0:
                    k -= 1
                elif tsum < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

        return ans

