class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1

        if x < 0:
            sign = -1
            x = abs(x)
        
        number = str(abs(x))
        length = len(number)
        res = ""
        val = 10

        for i in range(0,length):

            last = str(x%val)
            x = x//val

            res += last
        
        res = int(res) * sign

        if res > -2**31 and res < 2**31:
            return res

        else:
            return 0


            


             
            
        