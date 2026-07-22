class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sort_nums = sorted(nums)
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            if i > 0 and sort_nums[i] == sort_nums[i-1]:
                continue
            while start < end:
                arr = []
                if sort_nums[i] + sort_nums[start] + sort_nums[end] == 0:
                    arr.append(sort_nums[i])
                    arr.append(sort_nums[start])
                    arr.append(sort_nums[end])
                    result.append(arr)
                    start += 1
                    end -= 1
                    while start < end and sort_nums[start] == sort_nums[start - 1]:
                        start += 1
                    while start < end and sort_nums[end] == sort_nums[end + 1]:
                        end -= 1
                elif sort_nums[i] + sort_nums[start] + sort_nums[end] > 0:
                    end -= 1
                else:
                    start += 1
        return result
                
                

        