class Solution:
    def pascalTriangleI(self, r, c):
        result = []

        for i in range(r):
            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1] + result[i-1][j])

            result.append(row)

        return result[r-1][c-1]
