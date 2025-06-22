class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count=num=0
        # for i in nums:
        #     if count==0:
        #         num=i
        #     if num==i:
        #         count+=1
        #     else:
        #         count-=1
        # return num
        return sorted(nums)[len(nums)//2] 

