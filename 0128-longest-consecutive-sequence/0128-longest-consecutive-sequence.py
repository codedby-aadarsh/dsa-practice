class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        longest=0
        ans=set(nums)
        for i in ans:
            if i-1 not in ans:
                length=1
                curr=i
                while curr+1 in ans:
                    curr+=1
                    length+=1
                longest=max(longest,length)
        return longest

        