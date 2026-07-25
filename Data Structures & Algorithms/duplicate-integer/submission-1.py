class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_list = set()

        for num in nums:
            if num in set_list:
                return True
            else:
                set_list.add(num)
        
        return False