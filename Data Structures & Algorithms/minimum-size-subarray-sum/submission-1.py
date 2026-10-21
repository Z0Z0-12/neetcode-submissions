class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        output = float('inf')
        k_sum = 0

        for num in nums:
            k_sum += num
        
        if k_sum < target:
            return 0
        else:
            k_sum = nums[left]

        if nums[left] >= target:
            return 1

        for right in range(1, len(nums)):
            k_sum += nums[right]

            while k_sum >= target:
                if (right-left + 1) < output:
                    output = right - left + 1
                k_sum -= nums[left]
                left += 1
        
        return output