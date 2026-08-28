class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1 #1,2,3,4,5,6,7

        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                return mid
            
            elif nums[mid]>target:
                right=mid-1
            
            else:
                left=mid+1
        
        return -1
