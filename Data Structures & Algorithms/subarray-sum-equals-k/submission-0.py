class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            need = current_sum - k

            if need in prefix:
                count += prefix[need]
            
            if current_sum in prefix:
                prefix[current_sum] += 1
            else:
                prefix[current_sum] = 1
        
        return count