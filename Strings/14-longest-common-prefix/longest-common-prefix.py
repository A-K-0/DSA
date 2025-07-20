class Solution(object):
    def longestCommonPrefix(self, strs):
        sorted = strs.sort()

        word_1 = strs[0]  

        word_2 = strs[len(strs)-1]

        Output = []

        for i in range(min(len(word_1),len(word_2))):
            if word_1[i] == word_2[i]:
                Output.append(word_1[i])
            else:
                break

        return "".join(Output) 


        
        