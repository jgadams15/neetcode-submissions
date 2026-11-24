class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        for char in s:
            match char:
                case '(' | '[' | '{':
                    bracketStack.append(char)
                case ')':
                    if bracketStack and bracketStack[-1] == '(':
                        bracketStack.pop()
                    else:
                        return False
                case ']':
                    if bracketStack and bracketStack[-1] == '[':
                        bracketStack.pop()
                    else:
                        return False
                case  '}':
                    if bracketStack and bracketStack[-1] == '{':
                        bracketStack.pop()
                    else:
                        return False
                case _:
                    continue
        if(bracketStack):
            return False
        return True
                   

                