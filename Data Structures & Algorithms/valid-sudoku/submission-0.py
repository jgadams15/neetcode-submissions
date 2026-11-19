class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # essentially a duplicate check
        # if there is more than one number in a row, column, or box
        # sudoku is false.
        # we can do 3 iterations:
        # 1. Check for duplicates in each nested list
        #2. Check for duplicated in first item of each nested list
        # 3. Check first [0:3], [3:6], [6:9] items of each list

        #1: Checking in rows
        for row in board:
            duplicateCheck = set()
            for item in row:
                if(item == "."):
                    continue
                if item in duplicateCheck:
                    return False
                duplicateCheck.add(item)
        # 2: Checking in Columns
        for c in range(0,9):
            duplicateCheck = set()
            for row in board:
                if(row[c] == "."):
                    continue
                if(row[c] in duplicateCheck):
                    return False
                duplicateCheck.add(row[c])
        
        #3: Checking in Boxes
        # How do we do this?
            # Check first three items in first three rows 
            # check first three items in 2nd three rows
            # check first three items in last three rows
            # check second three items in first three
        for c in range(0, 9, 3):
            for r in range(0, 9, 3):
                duplicateCheck = set()
                for row in board[r:r+3]:
                    for item in row[c:c+3]:
                        if(item == "."):
                            continue
                        if(item in duplicateCheck):
                            return False
                        duplicateCheck.add(item)
        return True   

