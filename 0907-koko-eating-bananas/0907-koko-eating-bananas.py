class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)
        res=end 
        while start<=end:
            k=(start+end)//2

            ans = sum( math.ceil(i/k) for i in piles)
            if ans<=h:
                res=k
                end=k-1
            else:
                start=k+1
        return res
        