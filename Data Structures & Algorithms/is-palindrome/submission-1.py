class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")

        words = []

        for i in s:
            if i.isalnum():
                words.append(i)

        print(words)
        l, r = 0, len(words) - 1

        while l <= r:
            if words[l] != words[r]:
                return False
            
            l += 1
            r -= 1
        
        return True

