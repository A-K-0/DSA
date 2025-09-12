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

# * Traverse through the string and check if there is any vowel if there increase the value of the
#   variable and get to know how many vowels are there

# * create another variable in a different function which will go through the string and count vowels
#   ,if it contains 






class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """

        count = 0

        for char in s:
            if char == "a":
                count += 1

            if char == "e":
                count += 1

            if char == "i":
                count += 1
            
            if char == "o":
                count += 1
            
            if char == "u":
                count += 1

        if count == 0:
            return False

        if count % 2 == 0:
            return True

        if count % 2 != 0:
            return True

        
        