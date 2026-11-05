class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        res = {}
        l = 0
        r = 0
        
        for i in s1:
            freq[i] = freq.get(i , 0) + 1
        
        while r < len(s2):
            while r < len(s2) and s2[l] in s1:
                res[s2[r]] = res.get(s2[r] , 0) + 1
                if res[s2[l]] > freq[s2[l]]:
                    res[s2[l]] -= 1
                    l += 1
                if len(s1) == r - l + 1:
                    if res == freq:
                        return True
                    else:
                        res[s2[l]] -= 1
                        l += 1
                r += 1
            l += 1 
            r = l
            res.clear()
        return False
                