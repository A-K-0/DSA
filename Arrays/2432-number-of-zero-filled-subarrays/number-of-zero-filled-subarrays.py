class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = 0
        output = 0


        for i in range(len(nums)):
            if nums[i] == 0:
                zeros +=1 
                i += 1

            elif nums[i] != 0:
                output += (zeros*(zeros + 1))/2
                zeros = 0

        output += (zeros*(zeros + 1))/2

        return output

            







        