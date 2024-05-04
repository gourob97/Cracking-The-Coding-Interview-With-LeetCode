class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for index in range(len(s)-1):
            firstCharactersASCII = ord(s[index])
            secondCharactersASCII = ord(s[index+1])
            score += abs(firstCharactersASCII-secondCharactersASCII)
        return score