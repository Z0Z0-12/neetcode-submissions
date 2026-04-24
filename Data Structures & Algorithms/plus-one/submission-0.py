class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            temp = str(i)
            num = num + temp
        num = int(num) + 1

        list = []
        while num:
            digit = num % 10
            list.append(digit)
            num = num // 10
        list.reverse()
        return list
