class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        for idx, val in enumerate(nums):
            if dic[val] == 1:
                return val

            
        