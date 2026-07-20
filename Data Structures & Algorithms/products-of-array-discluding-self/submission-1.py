class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for i in nums:
            res.append(prefix)
            prefix = i * prefix
        index = len(res) - 1
        postfix = 1
        for x in reversed(res):
            res[index] = postfix * x
            postfix = postfix * nums[index]
            index -= 1

        return res
            

            