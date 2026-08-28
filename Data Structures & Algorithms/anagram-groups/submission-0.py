from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        for i in strs:
            z=str(sorted(i))
            h[z].append(i)
        li=[]
        for k,v in h.items():
            li.append(v)
        return li