class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=sum(nums)
        sum2=set(nums)
        return 2*sum(sum2)-sum1

            
        