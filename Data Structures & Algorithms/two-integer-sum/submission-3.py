class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        count=0
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in h:
                return [h[comp], i]
            h[nums[i]]=i
        return []