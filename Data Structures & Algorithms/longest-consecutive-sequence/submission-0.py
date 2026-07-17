class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0 
        for i in nums:
            counter = 0
            if (i - 1) not in hashset:
                length = 0
                while i + length in hashset:
                    counter += 1
                    length += 1
            if counter > longest:
                longest = counter

        return longest
            


        