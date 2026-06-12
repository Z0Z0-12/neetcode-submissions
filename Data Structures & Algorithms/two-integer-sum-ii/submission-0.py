class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = numbers[0]
        right = numbers[len(numbers)-1]
        
        for i in range(len(numbers)):
            if left + right > target:
                right = numbers[numbers.index(right)-1]
            elif left + right < target:
                left = numbers[numbers.index(left) + 1]
            else:
                return [numbers.index(left)+1, numbers.index(right)+1]

        return []