class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1=sorted(list(set(nums)))
        if len(nums1)>2:
            return nums1[-3]
        else:
            return nums1[-1]


        