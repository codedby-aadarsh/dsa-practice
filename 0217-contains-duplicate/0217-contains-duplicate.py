class Solution(object):
    def containsDuplicate(self, nums):
        
        s=set(nums)
        return not len(nums)==len(s) 
        