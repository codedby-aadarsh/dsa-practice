class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=sum(nums)
        sum2=set(nums)
        return 2*sum(sum2)-sum1

        # e.g= a=[a,a,b,b,c]  logic 
        # sum1=2a+2b+c
        # sum2=[a,b,c]
        # sum2=a+b+c
        # 2*sum2-sum1= 2a+2b+2c-(2a+2b+c)=c


            
        