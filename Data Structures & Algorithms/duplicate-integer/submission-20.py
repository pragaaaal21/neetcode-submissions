class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=len(nums)
        for i in range(0,x):
            for j in range(i+1,x):
                if nums[i]==nums[j]:
                    return True
        return False