from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        return [item for item, freq in Counter(nums).most_common(k)]

