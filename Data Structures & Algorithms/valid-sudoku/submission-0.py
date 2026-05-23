class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        # 1. Rows
        for row in board:
            seen_so_far = set()
            for digit in row:
                if digit != '.':
                    if digit not in valid_digits or digit in seen_so_far:
                        return False
                    seen_so_far.add(digit)

        # 2. Columns
        for i in range(9):
            seen_so_far = set()
            for x in range(9):
                digit = board[x][i]
                if digit != '.':
                    if digit not in valid_digits or digit in seen_so_far:
                        return False
                    seen_so_far.add(digit)

        # 3. 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen_so_far = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        digit = board[row][col]

                        if digit != '.':
                            if digit not in valid_digits or digit in seen_so_far:
                                return False
                            seen_so_far.add(digit)

        return True
        