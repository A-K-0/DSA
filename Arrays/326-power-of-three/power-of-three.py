class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''['1', '11', '1001', '11011', '1010001', '11110011', 
        '1011011001', '100010001011', '1100110100001', 
        '1001100110101011', '11100110101001001']'''

        if n < 1:
            
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return n == 1

    