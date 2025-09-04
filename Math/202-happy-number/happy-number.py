class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        hs = set()

        while n!= 1 and n not in hs:

            hs.add(n)

            total = 0
            for digits in str(n):
                total += int(digits) ** 2

            n = total


        return n == 1


        

            

            

            
            
        