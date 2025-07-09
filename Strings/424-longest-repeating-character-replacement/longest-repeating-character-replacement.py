class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        freq = {}
        max_count = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            max_count = max(freq[s[right]],max_count)

            if right - left + 1 - max_count > k:
                freq[s[left]] -= 1
                left += 1

        return len(s) - left        