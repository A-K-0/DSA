class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq  = [0] * 26

        MaxVow,MaxCons = 0,0

        for char in s:

            x = ord(char) - ord('a')

            if char in 'aeiou':

                freq[x] += 1
                MaxVow = max(MaxVow,freq[x])

            else:

                freq[x] += 1
                MaxCons = max(MaxCons,freq[x])

        return MaxVow + MaxCons