class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store a hashmap where the key is an array of numbers that
        # counts the frequency of the letters in the alphabet
        # and the values will be a list of strings
        hashmap = defaultdict(list)

        for i in strs:
            arr = [0] * 26
            for c in i:
                arr[ord(c) - ord('a')] += 1
            hashmap[tuple(arr)].append(i)

        return list(hashmap.values())
            
