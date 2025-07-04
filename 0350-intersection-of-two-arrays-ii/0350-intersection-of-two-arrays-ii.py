class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        res=[]
        for i in nums1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in nums2:
            if i in dic and dic[i]>0:
                res.append(i)
                dic[i]-=1
        return res