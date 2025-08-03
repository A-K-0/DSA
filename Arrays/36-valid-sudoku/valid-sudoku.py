class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        valid = set()
        i = 0

        #validate rows

        for row in board:
            for item in row:
                if item in valid:
                    return False
                elif item != '.':
                    valid.add(item)
                    # print(valid)
            
            valid.clear()

        
        # valid columns
        for i in range(9):
            for row in board:
                if row[i] in valid:
                    return False
                elif row[i] != '.':
                    valid.add(row[i])
                    print(valid)

            valid.clear()

        box_start = [(0,0),(0,3),(0,6),
                     (3,0),(3,3),(3,6),
                     (6,0),(6,3),(6,6)]

        for i,j in box_start:
            for row in range(i,i+3):
                for col in range(j,j+3):
                    item = board[row][col]

                    if item in valid:
                        return False
                    elif item != '.':
                        valid.add(item)
                        
            valid.clear()
        

        return True

        