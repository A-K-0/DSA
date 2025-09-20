class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1

        start = -1
        end = -1

        def leftend(left,right,start):
            while left <= right:

                mid = (left+right) // 2

                if nums[mid] < target:
                    left = mid+1

                elif nums[mid] > target:
                    right = mid - 1

                if nums[mid] == target:
                    start = mid
                    right = mid - 1

                print(mid)

            return start


        def rightend(left,right,end):
            while left <= right:

                mid = (left+right) // 2

                if nums[mid] < target:
                    left = mid+1

                elif nums[mid] > target:
                    right = mid - 1

                elif nums[mid] == target:
                    end = mid
                    left = mid + 1

                print(mid)

            return end
            

        return [leftend(left,right,start),rightend(left,right,end)]

        