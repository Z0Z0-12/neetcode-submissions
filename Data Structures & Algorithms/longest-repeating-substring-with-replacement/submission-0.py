class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        maximum_frequency = 0
        maximum_length = 0

        for right in range(len(s)):
            characters = s[right]

            counts[characters] = counts.get(characters, 0) + 1
            maximum_frequency = max(maximum_frequency, counts[characters])

            while(right - left + 1) - maximum_frequency > k:
                left_character = s[left]
                counts[left_character] -= 1
                left += 1 

            current_length = right - left + 1
            maximum_length = max(maximum_length, current_length)

        return maximum_length