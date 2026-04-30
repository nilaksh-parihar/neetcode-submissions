class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = []
        for u , i in enumerate(nums):
            mul = 1
            for v , j in enumerate(nums):
                if u == v:
                    continue
                else :
                    mul = mul * j
            list1.append(mul)
        
        return list1