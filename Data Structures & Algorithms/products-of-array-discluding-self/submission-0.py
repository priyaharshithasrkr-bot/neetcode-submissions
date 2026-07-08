class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Prefix products
        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]

        # Suffix products
        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans