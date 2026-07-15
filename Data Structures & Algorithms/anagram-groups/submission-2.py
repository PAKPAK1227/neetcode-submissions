class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store a hashmap where the key is an array of numbers that
        # counts the frequency of the letters in the alphabet
        # and the values will be a list of strings
        d = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for c in string:
                arr[ord(c) - ord('a')] += 1
            d[tuple(arr)].append(string)
        return list(d.values())

