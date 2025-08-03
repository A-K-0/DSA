class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        lookup = set(nums)
        Max = 1

        for num in lookup:
            next_num = num + 1 
            length = 1
            if num -1 not in lookup:
                while next_num in lookup:
                    length += 1
                    next_num += 1
                Max = max(length,Max)

        return Max
            

                




        