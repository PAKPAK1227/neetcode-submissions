class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        result = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if visited.get(difference) == None:
                visited[nums[i]] = i
            else:
                result.append(visited[difference])
                result.append(i)

        return result