class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        end = len(nums) - 1
        start = 0

        mid = (end + start)/2

        while start <= end:

            if nums[mid] > target:
                end = mid - 1

            elif nums[mid] < target:
                start = mid + 1

            elif nums[mid] == target:
                return mid 


            mid = (end + start)/2
            
        return -1


            




        