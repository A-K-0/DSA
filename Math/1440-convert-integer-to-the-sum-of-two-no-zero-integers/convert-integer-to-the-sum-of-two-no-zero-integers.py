class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):

            # num = n - i

            if '0' not in str(i) and '0' not in str(n - i):
                break

        return [i, n-i]

        