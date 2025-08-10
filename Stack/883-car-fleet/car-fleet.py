class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        #Distance = Speed/Time
        #Time = Distance/Speed

        stack = []
        merged = list(zip(position,speed))

        final = sorted(merged, key = lambda x : x[0], reverse=True)

        print(final)



        # stack.append(None)

        for item in final:
            Distance = target - item[0]
            Time = float(Distance) / item[1]

            if not stack or Time > stack[-1]:
                stack.append(Time)

            else:
                continue

        return len(stack)





        