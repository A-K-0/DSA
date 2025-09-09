class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        curr = 0

        for i in range(len(nums)):

            if count == 0:
                curr = nums[i]

            if curr == nums[i]:
                count += 1

            else:
                count -= 1

        return curr

        