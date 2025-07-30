class Solution(object):
    def containsDuplicate(self, nums):

        checker = set()

        for num in nums:
            if num in checker:
                return True
            
            else:
                checker.add(num)

        return False
        