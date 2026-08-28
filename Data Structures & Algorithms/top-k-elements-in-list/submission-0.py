from collections import Counter
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        res=sorted(nums, key=lambda x: -freq[x])
        
        # sort unique elements by frequency
        unique_nums = list(freq.keys())
        unique_nums.sort(key=lambda x: -freq[x])

        return unique_nums[:k]