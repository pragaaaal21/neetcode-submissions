class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for a in nums:
            x = nums
            x.remove(a)
            if a in x:
                return True
            
        return False

