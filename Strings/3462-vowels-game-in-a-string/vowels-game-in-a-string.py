# * In this question we have to understand whether in a game of substring removal who will win Alice
# or Bob, if Alice wins return True and if no return False

# EXAMPLES:

# 1)Input: s = "leetcoder"
#   Output: true

# 2)Input: s = "bbcd"
#   Output: false

# AIM:

# TIME COMP: O(n)
# SPACE COMP: O(1)


# INTUITION:

# * Alice - Odd
# * Bob - Even

# * NO NEED OF TOO MUCH THINKING

# * There is only one way bob is going to win which is a string having no vowels and all other cases 
#   return True as alice is going to win





class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """

        

        for char in s:
            if char in 'aeiou':
                return True

        return False

        
        