class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = {}
        for i, value in enumerate(nums):
            difference = target - value
            if not difference in hashmap.keys():
                hashmap[value] = i
            else:
                result.append(hashmap.get(difference))
                result.append(i)
                return result
        
            

            

