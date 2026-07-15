class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        result = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, v in count.items():
            freq[v].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            if freq[i] != False:
                for x in freq[i]:
                    result.append(x)
            if len(result) == k:
                break
        
        return result


    #   size of bucet array is max length
    #  we add + 1 when creating the buckets because the 0 bucket in 
    # the frequency list will always be empty cus each number appears
    # count frequency using hashmap
    # then do bucket sort but let the indexes be the frequency and the 
    # actual values of each array slot be attached in a list as the values in the list
    # then start at the max length because that will be the max frequency 
    #  of any value. Then go down



        