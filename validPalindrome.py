class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string =""
        for i in range(len(s)):
            if s[i].isalnum():
                clean_string+=s[i]
        start = 0
        end = len(clean_string)-1
        while start<end:
            if clean_string[start].upper() != clean_string[end].upper():
                return False
            start+=1
            end-=1
        return True
