class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        if not nums1:
            return None

        Curr = 0
        rock = -1 
        Max = -1
        nums1_stack = nums1[:]
        nums2_stack = nums2[:]
        res = []

        while nums1_stack:
            Curr = nums1_stack.pop()
            nums2_stack = nums2[:]

            while nums2_stack:
                rock = nums2_stack.pop()
                if rock > Curr:
                    Max = rock
                if rock == Curr:
                    break
            
            if Max == 0:
                res.append(-1)
            else:
                res.append(Max)

            Max = 0

        return res[::-1]



                




        