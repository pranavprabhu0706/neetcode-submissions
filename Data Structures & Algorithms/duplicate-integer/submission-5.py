class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortnums=sorted(nums)
        for i in range(len(sortnums)-1):
            if sortnums[i]==sortnums[i+1]:
                return True
        return False