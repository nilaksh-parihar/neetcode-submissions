class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        nums.sort()
        for i in range(0 , len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i + 1,len(nums) - 1
            while l<r:
                psum = nums[l] + nums[r] + nums[i]
                if psum > 0:
                    r -= 1
                elif psum < 0:
                    l += 1
                else :
                    out.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l - 1] and l<r:
                        l += 1
        return out

