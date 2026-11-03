class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxl = height[l]
        maxr = height[r]
        area = 0

        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                area += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                area += maxr - height[r]

        return area