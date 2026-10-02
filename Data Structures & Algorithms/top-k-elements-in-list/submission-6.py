class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary=defaultdict(int)

        for i in range(0,len(nums)):
            dictionary[nums[i]]+=1

        li=[]
        result=sorted(dictionary, key=lambda x:dictionary[x], reverse=True)
        
        return result[:k]