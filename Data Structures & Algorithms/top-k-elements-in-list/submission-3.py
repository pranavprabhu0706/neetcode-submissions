class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h={}
        for i in nums:
            h[i]=h.get(i,0)+1
        
        unique_list=list(h.keys())

        unique_list=sorted(unique_list, key=lambda x: -h[x])

        return unique_list[:k]