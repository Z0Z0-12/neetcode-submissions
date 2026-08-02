class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        current = (left + right) // 2

        while left <= right:
            if nums[current] == target:
                return current
            
            if nums[current] > target:
                right = current - 1
                current = (right + left) // 2
            else:
                left = current + 1
                current = (left + right) // 2
        
        return -1


        