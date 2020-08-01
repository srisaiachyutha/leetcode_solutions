class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #here we precompute the sum's of the ranges and we just extract after that

        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j]+=matrix[i][j-1]
            if i>0:
                for j in range(len(matrix[0])):
                    matrix[i][j]+=matrix[i-1][j]
        self.m=matrix
                    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1>0 and row1>0:
            #if the given parameters are greater than 0th row and 0th column
            return self.m[row2][col2]-self.m[row2][col1-1]-self.m[row1-1][col2]+self.m[row1-1][col1-1]
        elif col1>0:
            #if the given row1 parameter is equal to the initial or 0th row
            return self.m[row2][col2]-self.m[row2][col1-1]
        elif row1>0:
            #if the give col1 parameter is equal to the initial col
            return self.m[row2][col2]-self.m[row1-1][col2]
        else:
            #if both the col1 and row1 are the 0 
            return self.m[row2][col2]
