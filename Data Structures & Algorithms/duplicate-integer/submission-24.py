class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for a in nums:
            nums.remove(a)
            if a in nums:
                return True
            
        return False

