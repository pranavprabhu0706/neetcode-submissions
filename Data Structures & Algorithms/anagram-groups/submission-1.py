from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        li=[]

        for i in strs:
            sword="".join(sorted(i))
            d[sword].append(i)
        
        for k,v in d.items():
            li.append(v)
        
        return li