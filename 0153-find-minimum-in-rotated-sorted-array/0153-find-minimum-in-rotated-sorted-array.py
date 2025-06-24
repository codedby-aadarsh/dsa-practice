class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[0]
        low,high=0,len(nums)-1
        while high-low>1:
            mid=(high+low)//2
            if nums[mid]<nums[low]:high=mid
            elif nums[mid]>nums[high]: low=mid
            else: return nums[low]
        return min(nums[low],nums[high])