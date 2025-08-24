class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Max = 0 
        z_count = 0
        o_count = 0
        n = len(nums)
        j = 0
        i = 0

        while j < n:

            if nums[j] == 1:
                o_count += 1
                j += 1

            elif nums[j] == 0:
                z_count += 1

                if z_count > 1:
                    while nums[i] != 0:
                        if nums[i] == 1:
                            o_count -= 1
                        i += 1
                   
                    i += 1
                    z_count -= 1

                j += 1   
            Max = max(Max, j - i)

        return Max-1
