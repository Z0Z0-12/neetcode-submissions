class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
    
        nums = list(set(nums))
        nums.sort()
        seq = {}
        current_count = 0
        j = 1

        for i in range(len(nums)-1):
            if abs(nums[i+1] - nums[i]) == 1:
                current_count += 1
            else:
                seq[j] = current_count + 1
                j += 1
                current_count = 0

        seq[j] = current_count + 1

        values = list(seq.values())
        maximum = max(values)

        return maximum

