from collections import Counter
class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """

        counter = Counter()

        if n==1:
            return True

        # while n> 0:
        #     num = n%10
        #     counter[num] += 1
        #     n //= 10

        counter = Counter(str(n))

        for i in range(31):
            if Counter(str(1 << i)) == counter:
                return True
        return False


        
        