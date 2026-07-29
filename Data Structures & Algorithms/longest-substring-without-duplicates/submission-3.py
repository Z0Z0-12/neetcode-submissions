class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lister = set()
        l, r = 0, 0
        maximum  = 0

        while r < len(s):
            if s[r] not in lister:
                lister.add(s[r])
                maximum = max(maximum, len(lister))
                r += 1
            else:
                lister.remove(s[l])
                l += 1
        
        return maximum
        