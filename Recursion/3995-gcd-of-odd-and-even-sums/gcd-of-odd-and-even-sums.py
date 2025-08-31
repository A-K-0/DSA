import math
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        EvenSum = 0
        OddSum = 0

        if n == 1:
            return 1

        for i in range(1,n*2+1):
            if i%2 == 0:
                EvenSum += i

            else:
                OddSum += i

        def GCD(EvenSum, OddSum):
            
            OddSum = EvenSum % OddSum
            temp = EvenSum
            EvenSum = OddSum

            if OddSum == 0:
                return temp
 
            return GCD(EvenSum,OddSum)

        return GCD(EvenSum,OddSum)





        