class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()

        left = 0
        maximum = 0

        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            characters.add(s[right])

            current_length = len(characters)
            maximum = max(maximum, current_length)
        
        return maximum
        