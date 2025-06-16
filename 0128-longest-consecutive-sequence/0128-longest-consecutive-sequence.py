class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = sorted(set(nums))
        max_count = 1# this keep tracks of the longest sequence 
        count = 1 #if there is a gap in sequence where other sequence starts then  you keep track of that one by this by reseting the original one 
        for i in range(1, len(ans)):
            if ans[i] == ans[i-1] + 1:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count