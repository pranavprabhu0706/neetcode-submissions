class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        res=0

        for i in s:
            if i-1 in s:
                continue
            else:
                q=i
                c=1
                while q+1 in s:
                    c+=1
                    q=q+1
                res=max(res, c)
        
        return res
