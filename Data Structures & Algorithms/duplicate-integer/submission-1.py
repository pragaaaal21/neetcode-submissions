class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      nums.sort()
      n=len(nums)
      for i in range(0,n):
        if (i==nums[i]):
            return True
      return False
            