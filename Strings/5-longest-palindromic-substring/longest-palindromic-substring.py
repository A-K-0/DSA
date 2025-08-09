class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        length = len(s)
        output = ''


        if length <= 1:
            return s
        
        output = s[0] 

    
        for i in range(length):

            l, r = i, i
            while l >= 0 and r < length and s[l] == s[r]:
                if (r - l + 1) > len(output):
                    output = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < length and s[l] == s[r]:
                if (r - l + 1) > len(output):
                    output = s[l:r+1]
                l -= 1
                r += 1

        return output





        

           


       
        