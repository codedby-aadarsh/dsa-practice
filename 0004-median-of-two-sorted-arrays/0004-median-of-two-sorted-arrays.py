class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not len(nums1):
            return mid(nums2)
        elif not len(nums2):
            return mid(nums1)
        else:
            nums =nums1+nums2
            nums.sort()
            return mid(nums)
def mid(nums):
    mid1=len(nums)//2
    if len(nums)%2==0:
        return (nums[mid1]+nums[mid1-1])/2.0
    else:
        return float(nums[mid1])

        