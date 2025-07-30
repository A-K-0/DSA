class Solution(object):
    def containsDuplicate(self, nums):
        
        if nums is None:
            return False

        checker = set()

        for num in nums:
            if num in checker:
                return True
            
            else:
                checker.add(num)

        return False
        