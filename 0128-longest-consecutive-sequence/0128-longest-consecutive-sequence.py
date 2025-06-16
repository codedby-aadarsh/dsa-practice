class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        longest=0
        #first you gotta make the list into the set, by doing this we make sure there are no redundant elements in it
        ans=set(nums)
        for i in ans:
            if i-1 not in ans:# here we check is there any elements less than the current one by 1. and if this element is already counted. as other sequence start element in the set will have a conisderably gap.
                length=1
                curr=i
                while curr+1 in ans: # checking the consecutive element
                    curr+=1#incrementing the current 
                    length+=1
                longest=max(longest,length)#comparing with the past longest sequence 
        return longest

        