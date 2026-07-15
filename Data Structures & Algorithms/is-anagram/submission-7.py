class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
            t_hashmap[t[i]] = t_hashmap.get(t[i], 0) + 1
        
        for i in s_hashmap:
            if s_hashmap.get(i) != t_hashmap.get(i):
                return False
        return True


        