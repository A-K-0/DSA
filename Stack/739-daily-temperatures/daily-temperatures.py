class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        output = [0] * n
        stack = []

        
        for i in range(n):
            
            while stack and temperatures[i] > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                output[prev_index] = i - prev_index

            stack.append((temperatures[i], i))

        return output


