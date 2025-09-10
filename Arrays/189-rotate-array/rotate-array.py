
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def reverse(nums,left,right):

            while left < right:

                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1

            return nums


        n = len(nums) - k - 1
        k = k % len(nums)

        if k == 0:
            return nums

        nums.reverse()

        reverse(nums,0,k-1)

        reverse(nums,k,len(nums)-1)

        return nums
