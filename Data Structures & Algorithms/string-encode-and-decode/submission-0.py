class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            
            final = final + f"{len(s):03d}" + s
        return(final)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = int(s[i:i+3])  # read length
            i += 3

            result.append(s[i:i+length])  # read string
            i += length

        return result
