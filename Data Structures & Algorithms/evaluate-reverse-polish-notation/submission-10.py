class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        for v in tokens:
            try:
                vals.append(int(v))

            except ValueError:
                if v == '+':
                    val = vals.pop() + vals.pop()

                    vals.append(val)
                elif v == '-':
                    v1 = vals.pop()
                    v2 = vals.pop()
                    val = v2 - v1
                    vals.append(val)
                elif v == '*':
                    val = vals.pop() * vals.pop()
                    vals.append(val)
                else:
                    v1 = vals.pop()
                    v2 = vals.pop()
                    val = int(v2 / v1)
                    vals.append(val)
        return vals.pop()