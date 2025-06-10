class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        sum=0
        for i in nums:
            sum+=i
            li.append(sum)
        return li

        