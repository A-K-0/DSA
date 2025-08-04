class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(numbers) - 1

        while l < r:

            if target < numbers[l] + numbers[r]:
                r -= 1

            elif target > numbers[l] + numbers[r]:
                l += 1

            # if target == numbers[l] + numbers[r]:
            else:
                return [l+1,r+1]

        return []

            

        