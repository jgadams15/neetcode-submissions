class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Operands are in order of what they are done in
        # Push numbers to a stack
        # when you hit an operand, pop 2 numbers from stack, calculate with operand
        # push back to stack,
        # at the end, there should be one number in the stack
        # that is your final calculation
        varStack = []
        for c in tokens:
            match c:
                case '+' | '-' | '*'| '/':
                    const2 = varStack.pop()
                    const1 = varStack.pop()
                    if(c == "+"):
                        varStack.append(const1 + const2)
                    elif(c == "-"):
                        varStack.append(const1 - const2)
                    elif(c == "*"):
                        varStack.append(const1 * const2)
                    elif(c == "/"):
                        # // becasue we want integer division
                        varStack.append(int(const1 / const2))
                case _:
                    varStack.append(int(c))
        return varStack.pop()
            
