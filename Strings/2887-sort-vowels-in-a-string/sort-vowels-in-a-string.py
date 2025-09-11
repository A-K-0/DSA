class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        look = set("AEIOUaeiou")
        vowels = []
        res = []
        i = 0

        for char in str(s):
            if char in look:
                vowels.append(char)

            i += 1

        vowels.sort(key=lambda x: x[0])

        j = 0

        for char in s:
            if char in look:          
                res.append(vowels[j])
                j += 1
            else:                 
                res.append(char)

        return "".join(res)


        

        



        print(vowels)



        