class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum_area = 0

        while left < right:
            if heights[left] < heights[right]:
                area = heights[left] * (right - left)
                left += 1
            elif heights[left] >= heights[right]:
                area = heights[right] * (right - left)
                right -= 1
            if area > maximum_area:
                maximum_area = area
                
        return maximum_area