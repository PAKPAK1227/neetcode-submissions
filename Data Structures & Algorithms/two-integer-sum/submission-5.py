class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashMap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashMap:
                result.append(hashMap.get(difference))
                result.append(i)
            else:
                hashMap[n] = i
        return result
            

