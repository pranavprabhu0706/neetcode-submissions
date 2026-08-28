class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        flag=0

        l=len(nums)
        for i in range(0,l-1):
            if(nums[i]==nums[i+1]):
                return True
        return False