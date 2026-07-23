class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrms = {}
        out = []
        for s in strs:
            sort = "".join(sorted(s))
            if sort in angrms:
                angrms[sort].append(s)
            else:
                angrms[sort] = [s]

        return list(angrms.values())