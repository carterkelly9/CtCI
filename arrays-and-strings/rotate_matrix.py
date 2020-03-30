# 1.7
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.
# Can you do this in place?

# in place - O(n^2) time, O(1) space
def rotate_matrix(n):
    matrix = [[i for i in range(n)] for j in range(n)]

    for i in range(n // 2):
        first = i
        last = n - 1 - i
        for j in range(first, last):
            offset = j - first
            temp = matrix[first][j]
            matrix[first][j] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[j][last]
            matrix[j][last] = temp