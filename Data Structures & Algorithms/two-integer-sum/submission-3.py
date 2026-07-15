class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if not difference in hashmap:
                hashmap[n] = i
            else:
                if i < hashmap[difference]:
                    result.append(i)
                    result.append(hashmap[difference])
                else:
                    result.append(hashmap[difference])
                    result.append(i)
        return result
        


