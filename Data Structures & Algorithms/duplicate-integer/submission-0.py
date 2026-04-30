class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        for i in nums:
            if nums.count(i) > 1:
                return True
            else :
                continue
        return False

