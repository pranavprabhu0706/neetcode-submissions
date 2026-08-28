class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # len of nums
        n=len(nums)

        # declare left and right as 1
        left=1
        right=1

        # declare left and right list with 
        # len of nums and fill it with 0
        l_li=[0]*n
        r_li=[0]*n

        # l_li initialize the list with left (left=1) 
        # and multiply all the elements from left to right 
        # and update the value in left
        for i in range(n):
            # initialize j with n-i-1
            j=n-i-1
            l_li[i]=left
            left=left*nums[i]

        # initialize r_li with right where right=1
        # and multiply all the elements from right to left
        # and update the value in right
            r_li[j]=right
            right=right*nums[j]

        # multiply l_li[i] and r_li[i] and return it (use zip() function)
        return [l*r for l,r in zip(l_li, r_li)]