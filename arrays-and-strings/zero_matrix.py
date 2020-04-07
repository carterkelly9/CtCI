# 1.8
# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.

# in place - O(MN) time, O(1) space
def zero_matrix():
    # example matrix
    matrix = [[1, 2, 3, 4], [3, 1, 4, 2], [1, 2, 3, 4], [4, 3, 2, 0]]

    # check if the first row/column has a zero
    first_row_zero = False
    first_col_zero = False

    for i in matrix[0]:
        if i == 0:
            first_row_zero = True
    
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_zero = True

    # check the rest of the matrix for zeros, use the first row/column as identifiers
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # use the first row/column to set rows/columns as all zero
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[i][j] = 0

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1, len(matrix)):
                matrix[i][j] = 0

    # if there was a zero in the initial first row/column, 
    if first_row_zero == True:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    if first_col_zero == True:
        for i in range(len(matrix)):
            matrix[i][0] = 0