class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i,j in zip(nums,index):
            ans.insert(j,i)
        return ans

        