class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        for v in tokens:
            try:
                vals.append(int(v))

            except ValueError:
                num2 = vals.pop()
                num1 = vals.pop()
                if v == '+':
                    vals.append(num1+num2)
                elif v == '-':
                    vals.append(num1-num2)
                elif v == '*':
                    vals.append(num1*num2)
                else:
                    vals.append(int(num1/num2))
        return vals.pop()