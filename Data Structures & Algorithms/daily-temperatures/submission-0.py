class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            
            while len(stack) > 0 and val > temperatures[stack[-1]]:
                value = stack.pop()
                result[value] = i - value
            stack.append(i)
            
        return result


        