class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        # Step 1: Calculate prefix product for each index
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Step 2: Multiply by suffix product for each index
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


        
        