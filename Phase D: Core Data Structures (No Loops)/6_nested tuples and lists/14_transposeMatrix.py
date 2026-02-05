# Goal: Transpose a 2D list (matrix)
# Expected outcome: running this file prints exactly: [[1, 4], [2, 5], [3, 6]]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# TODO: build transposed (3x2) so transposed[i][j] == matrix[j][i]
transposed = [[matrix[j][i] for j in range(len(matrix))]
              for i in range(len(matrix[0]))]

print(transposed)
