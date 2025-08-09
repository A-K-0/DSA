class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n < 0:
            return False

        binary = bin(n)

        return binary.count("1") == 1