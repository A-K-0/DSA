import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """


        def k_determine(k):

            hrs = 0
            for p in piles:
                hrs += (p + k - 1) // k 
            
            return hrs <= h


        l = 1
        r = max(piles)

        while l < r:
            k = (l+r) // 2

            if k_determine(k):
                r = k

            else:
                l = k+1

        return r

        
       
        





        