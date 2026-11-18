class Solution:        
    def hasDuplicate_2(self, nums: list[int]) -> bool:
        nums_count = {}
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        return not all(nums_count[num] == 1 for num in nums_count)
    
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
