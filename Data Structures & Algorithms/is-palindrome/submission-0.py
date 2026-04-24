class Solution:
    def isPalindrome(self, s: str) -> bool:
        charList = []

        for ch in s:
            if ch.isalnum():
                charList.append(ch.lower())

        word = "".join(charList)

        backCount = -1

        for i in range(len(word) // 2):
            if word[i] != word[backCount]:
                return False
            backCount -= 1
        
        return True