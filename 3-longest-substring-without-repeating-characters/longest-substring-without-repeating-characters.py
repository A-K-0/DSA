class Solution(object):
    def lengthOfLongestSubstring(self, s):
        SET = set()
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in SET:
                SET.remove(s[left])
                left += 1
            
            SET.add(s[right])
            res = max(res,right-left+1)

        return res
        