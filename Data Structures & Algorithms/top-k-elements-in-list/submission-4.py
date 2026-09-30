class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary=defaultdict(int)
        s=set()

        for i in range(0,len(nums)):
            dictionary[nums[i]]+=1
        
        result=sorted(dictionary, key=lambda x: dictionary[x], reverse=True)

        li=[]
        for j in range(0, k):
            li.append(result[j])
        
        return li