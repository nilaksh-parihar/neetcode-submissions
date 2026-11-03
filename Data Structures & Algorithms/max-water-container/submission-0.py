class Solution:
    def maxArea(self, height: list[int]) -> int:
        l , r ,area= 0, len(height) - 1 , 0
        while l<r:
            temp = min(height[l] , height[r]) * (r-l)
            area = max(temp , area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area