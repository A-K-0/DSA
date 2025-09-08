class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):

            num = n - i

            if '0' not in str(num) and '0' not in str(n - num):
                break

        return [n-num, num]

        