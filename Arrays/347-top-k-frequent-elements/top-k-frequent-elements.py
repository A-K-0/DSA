class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1 
            if num not in count:
                count[num] = 1
                
        sorted_items = sorted(count.items(), key=  lambda x : x[1], reverse = True)
        # print(sorted_items)

        output = [item[0] for item in sorted_items[:k]]

        return output
        

        