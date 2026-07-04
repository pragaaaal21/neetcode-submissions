class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        select =set()
        for num in nums:
            if num in select:
                return True
            select.add(num)
        return False