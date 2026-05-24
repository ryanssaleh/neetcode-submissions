class NumMatrix:
    matrix: list[list[int]]
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_so_far = 0
        for row_range in range(row1, row2 + 1):
            row = self.matrix[row_range]
            sum_so_far += sum(row[col1: col2 + 1])
        return sum_so_far
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)