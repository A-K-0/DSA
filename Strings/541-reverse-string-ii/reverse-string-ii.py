# *We have to reverse a string on uptill k part of string and the other part of the 2k must be 
#  left like that only

# EXAMPLES:

# 1)Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# 2)Input: s = "abcd", k = 2
# Output: "bacd"

# INTUITION:

# * Will use a function with reverseing duty
# * Will use 2 pointer approach to get the points till which we must reverse and to go to the next point too


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        def reverse(left,right):

            while left < right:

                s[left], s[right] = s[right], s[left]   

                left += 1
                right -= 1

        n = len(s)
        s = list(s) 

        for i in range(0,n,2*k):

            end = min(i+k-1,n-1)
            rev = reverse(i,end)
            print(i,end)

        return ''.join(s)

           

            

             

            