class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if len(digits)==0:
        #     return [1]
        # elif digits[-1]!=9:
        #     digits[-1]+=1
        #     return digits
        # else:
        #     res=[]
        #     carr=0
        #     digits[-1]+=1
        #     for i in digits[::-1]:
        #         res.append((i+carr)%10)
        #         carr=(i+carr)//10
        #     if carr:
        #         res.append(carr)
        #     return res[::-1]
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we reach here, it means all digits were 9
        # We need to add a new digit at the beginning
        return [1] + digits

            


