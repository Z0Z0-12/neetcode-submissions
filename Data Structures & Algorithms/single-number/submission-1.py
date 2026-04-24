class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, -1, -2):
            temp = nums[i]
            nums.remove(nums[i])
            if temp in nums:
                nums.remove(temp)
            else:
                return temp
        return nums[0]