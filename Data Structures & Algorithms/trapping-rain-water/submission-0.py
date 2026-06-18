class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        trapped_water = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if height[left] < height[right]:
                trapped_water += left_max - height[left]
                left += 1
            else:
                trapped_water += right_max - height[right]
                right -= 1

        return trapped_water
