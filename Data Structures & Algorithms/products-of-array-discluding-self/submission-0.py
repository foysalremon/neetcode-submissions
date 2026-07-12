class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        suffix_arr = [1] * (length + 2)
        preffix_arr = [1] * (length + 2)
        res = [0] * length

        for i in range(length):
            suffix_arr[i + 1] = suffix_arr[i] * nums[i]
            preffix_arr[length - i] = preffix_arr[length - i + 1] * nums[length - i - 1]

        for i in range(length):
            res[i] = suffix_arr[i] * preffix_arr[i + 2]

        return res