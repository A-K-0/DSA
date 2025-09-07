import math
class Solution(object):
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """

        # Bézout’s theorem says:

        # (X + Y) == Target

        #     OR

        # gcd(x,y)=m⋅x+n⋅y

        # - Here it means that at some value of m and n the answer will be equal to GCD(x,y)'s multiple 

        # - The target can't exceed X+Y => Target, so this is one of the condition to check 

        if target <= x+y:

            if target == x+y:
                return True

            elif target % math.gcd(x,y) == 0:
                return True

            else:
                return False
        else:
            return False

        

                 