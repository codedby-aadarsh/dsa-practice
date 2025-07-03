class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1,p2=0,len(height)-1
        res=0
        while p1<=p2:
            if height[p1]==height[p2]:
                vol=height[p1]*abs(p2-p1)
                p1+=1
                p2-=1
            elif height[p1]>height[p2]:
                vol= height[p2]*abs(p2-p1)
                p2-=1
            else:
                vol= height[p1]*abs(p2-p1)
                p1+=1
            if vol>=res:
                res=vol
        return res
            