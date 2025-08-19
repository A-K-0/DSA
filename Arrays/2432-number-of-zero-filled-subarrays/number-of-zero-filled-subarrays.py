class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        j = 0
        zeros = 0
        output = 0

        # while i and j:

        #     if nums[j] == 0:
        #         zeros += 1
        #         j += 1

        #     elif nums[j] != 0:
        #         output += (zeros(zeros + 1))/2
        #         zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros +=1 
                i += 1

            elif nums[i] != 0:
                output += (zeros*(zeros + 1))/2
                zeros = 0

        output += (zeros*(zeros + 1))/2

        return output

            







        