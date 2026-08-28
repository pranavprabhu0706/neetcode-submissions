from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #create a dictionary to store nums and count of it
        freq=Counter(nums)

        #create another list to store the keys
        unique_nums=list(freq.keys())

        # sort the list by decreasing frequency
        unique_nums=sorted(freq.keys(), key=lambda x: -freq[x])

        # return the keys till k
        return unique_nums[:k]