class Solution(object):
    def maxSubArray(self, nums):
        curr_max = nums[0]
        MAX = nums[0]


        for i in range(1,len(nums)):
            
            curr_max = max(nums[i],curr_max+nums[i])
            MAX = max(MAX, curr_max)

        return MAX
        