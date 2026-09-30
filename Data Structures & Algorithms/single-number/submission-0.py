class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary=defaultdict()

        for i in range(0,len(nums)):
            count=1
            if nums[i] in dictionary:
                count+=1
            
            dictionary[nums[i]]=count
        
        for key,value in dictionary.items():
            if value==1:
                return key