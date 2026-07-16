class Solution:

    # encode hte strings by putting the length of each string (stored as an integer)
    # folllowed by a "#" sign before each word and use the hash as a delimeter
    # then
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #very pythonic way of assinging two variables

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

        # i is the start of each new string, j is what keeps track of the values
        # in each string and how you stop before you get the delimeter
        
        


