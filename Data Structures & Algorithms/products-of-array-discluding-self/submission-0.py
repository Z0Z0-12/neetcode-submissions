import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        nums_len = len(nums)
        for i in range(nums_len):
            number = nums[0]
            nums.remove(number)
            product = math.prod(nums)
            result.append(product)
            nums.append(number)
        
        return result
