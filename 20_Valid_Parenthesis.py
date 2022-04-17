class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        stack = []
        
        
        for i in range(len(s)):
            if s[i] in d.keys():
                stack.append(s[i])
            elif len(stack)==0:
                return False
            else:
                if d[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        
        if len(stack)==0:
            return True
        return False
            
            
        
        
        
