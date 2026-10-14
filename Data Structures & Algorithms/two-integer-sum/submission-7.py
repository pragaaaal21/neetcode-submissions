class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i,num in enumerate(nums):
            d = target-num
            if d in hm:
                return [hm[d],i]
            hm[num]=i