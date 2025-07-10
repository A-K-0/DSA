class Solution(object):
    def isAnagram(self, s, t):
        s_freq = {}
        t_freq = {}

        for i in range(len(s)):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1

        for j in range(len(t)):
            t_freq[t[j]] = t_freq.get(t[j], 0)+1

        if s_freq == t_freq:
            return True
        else:
            return False
        

        