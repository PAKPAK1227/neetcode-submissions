class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if hashmap.get(difference) == None:
                hashmap[nums[i]] = i
            else:
                if i < hashmap[difference]:
                    result.append(i)
                    result.append(hashmap[difference])
                else:
                    result.append(hashmap[difference])
                    result.append(i)
        return result
        


