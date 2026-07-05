class Solution:
    def setZeroes(self, matrix):
        # Your code goes here
        self.matrix = matrix   # missing
        # print(len(matrix))
        for i in  range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if matrix[i][j] == 0:
                    self.mark_row(i)
                    self.mark_col(j)
        for i in  range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        return self.matrix

    def mark_row(self, i):
        for j in range(len(self.matrix[i])):
            if self.matrix[i][j] != 0:
                self.matrix[i][j] = -1

    def mark_col(self, j):
        for i in range(len(self.matrix)):
            if self.matrix[i][j] != 0:
                self.matrix[i][j] = -1
        
