class Solution:
    def plusOne(self, dig: List[int]) -> List[int]:
        for pos in range(len(dig)-1,-1,-1):
            if dig[pos]<9:
                dig[pos]+=1
                return dig
            elif dig[pos]>=9:
                dig[pos]=0
        return [1]+dig

                

    