class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        left = 0
        right = len(height)-1
        Max = 0

        while left < right:

            area = min(height[right],height[left]) * (right - left)
            Max = max(area,Max)

            if height[left] > height[right]:
                right = right - 1
            
            elif height[left] < height[right]:
                left = left + 1

            else:
                right = right - 1

            # if height[left] == height[right]:

            #     if height[left+1] > height[right-1]:     

        return Max

