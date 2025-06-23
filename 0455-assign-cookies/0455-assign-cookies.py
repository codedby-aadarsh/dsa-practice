class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        res=0
        i=0
        while res<len(g) and i<len(s):
            if s[i]>=g[res]:
                res+=1
            i+=1
        return res