class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        for char in s:
            if char in s_dict.keys():
                s_dict[char]+=1
            else:
                s_dict[char] = 1
                
        for char in t:
            if char in t_dict.keys():
                t_dict[char]+=1
            else:
                t_dict[char] = 1
        
        if s_dict.keys() == t_dict.keys():
            
            for key in s_dict.keys():
                if t_dict[key] == s_dict[key] :
                    continue
                else:
                    return False
            return True

