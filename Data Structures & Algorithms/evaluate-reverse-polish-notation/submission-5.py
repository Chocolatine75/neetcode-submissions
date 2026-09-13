class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        num = []
        for t in tokens:
  
            if t == '+':
                n1 = num.pop()
                n2 = num.pop()
                num.append(n2+n1)
            elif t == '-':
                n1 = num.pop()
                n2 = num.pop()
                num.append(n2-n1)
            elif t == '*':
                n1 = num.pop()
                n2 = num.pop()
                num.append(n2*n1)
            elif t == '/':
                n1 = num.pop()
                n2 = num.pop()
                num.append(int(n2/n1))
            else:
                num.append(int(t))
        return num.pop()
            



