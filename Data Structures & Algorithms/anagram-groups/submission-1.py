class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            counter = [0] * 26
            for character in string:
                counter[ord(character) - ord('a')] += 1
            
            hashmap[tuple(counter)].append(string)
        
        return list(hashmap.values())


        