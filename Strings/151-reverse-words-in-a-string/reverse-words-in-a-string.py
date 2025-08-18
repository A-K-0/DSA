class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        Final = ""
        st = ""

        for char in s:

          if char != " ":
            st = st + char

          elif char == " ":
            if st:
              Final = (st + " " + Final) if Final else st
            st = ""

        if st:
          Final = (st + " " + Final) if Final else st


        return Final






        