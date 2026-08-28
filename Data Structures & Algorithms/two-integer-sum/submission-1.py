class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        l=len(nums)

        for i in range(0,l):
            comp=target-nums[i]

            if comp in h and h[comp]!=i:
                return [h[comp], i]
            
            h[nums[i]]=i