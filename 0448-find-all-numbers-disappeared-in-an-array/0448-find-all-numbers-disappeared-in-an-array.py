class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans=set(nums)
        return [i for i in range(1, len(nums)+1) if i not in ans]