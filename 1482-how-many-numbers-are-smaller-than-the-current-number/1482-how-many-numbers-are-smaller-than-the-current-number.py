class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            min=0
            val=i
            for j in nums:
                if val>j:
                    min+=1
            ans.append(min)
        return ans
                

            
        