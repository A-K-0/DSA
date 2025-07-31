from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        group_anagram = defaultdict(list)

        for s in strs:
            counter = [0]*26

            for c in s:
                counter[ord(c) - ord('a')] += 1
            
            key = tuple(counter)

            group_anagram[key].append(s)

        return group_anagram.values()
        