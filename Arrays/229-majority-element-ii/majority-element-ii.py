
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        Num2 = None
        Num1 = None
        count1 = 0
        count2 = 0
        res = []

        for num in nums:

            if num == Num1:
                count1 += 1

            elif num == Num2:
                count2 += 1

            elif count1 == 0:
                Num1,count1 = num,1

            elif count2 == 0:
                Num2,count2 = num,1

            else:

                count1,count2 = count1 - 1,count2 - 1

        for n in [Num1,Num2]:
            if n is not None and nums.count(n) > len(nums) / 3:
                res.append(n)


        return res

        
        