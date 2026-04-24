class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while (stack and t > stack[-1][0]):
                pastTemp, pastIndex = stack.pop()
                res[pastIndex] = i - pastIndex
            stack.append((t, i))
        return res