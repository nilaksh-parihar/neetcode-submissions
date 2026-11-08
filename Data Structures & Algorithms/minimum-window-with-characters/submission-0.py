class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) : return ""
            

        freq = {}
        window = {}

        for c in t:
            freq[c] = freq.get(c, 0) + 1

        l = 0
        have = 0
        need = len(freq)

        res = [-1, -1]
        resLen = float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in freq and window[c] == freq[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -= 1

                l += 1

        return "" if resLen == float('inf') else s[res[0]:res[1] + 1]