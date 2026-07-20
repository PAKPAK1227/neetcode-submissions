class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for x in range(len(nums)):
                if x == i:
                    continue
                else:
                    product = product * nums[x]
            res.append(product)

        return res