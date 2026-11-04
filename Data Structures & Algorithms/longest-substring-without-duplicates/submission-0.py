class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        longest = 1
        if not s:
            return 0 
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
                r -= 1
            longest = max(longest , r - l + 1)
            r += 1
        return longest