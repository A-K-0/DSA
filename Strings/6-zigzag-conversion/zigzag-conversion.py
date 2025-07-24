class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1:
            return s

        

        i = 0
        d = 1

        char = [[] for _ in range(numRows)]

        for j in range(len(s)):
            char[i].append(s[j])

            if i == 0:
                d = 1

            elif i == numRows-1:
                d = -1

            i += d 

        ret =''
        for i in range(numRows):
            ret += ''.join(char[i])

        return ret

            

       
        