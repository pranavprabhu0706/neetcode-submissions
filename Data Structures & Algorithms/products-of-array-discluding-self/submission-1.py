class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_arr=[1]
        r_arr=[1]
        left=1
        right=1

        for i in range(0,len(nums)-1):
            s=nums[i]
            left=left*s
            l_arr.append(left)
        
        for j in range(len(nums)-1,0,-1):
            s=nums[j]
            right=right*s
            r_arr.append(right)
        
        s_arr=r_arr[::-1]

        print(l_arr)
        print(s_arr)

        return [i*j for i,j in zip(l_arr,s_arr)]