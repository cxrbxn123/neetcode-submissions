class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dicts = {}
        for s in strs:
            new = ''.join(sorted(s))
            if new in dicts:
                dicts[new].append(s)
            else:
                dicts[new] = [s]
        
        return list(dicts.values())