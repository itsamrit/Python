# Count Square Submatrices with All ones in a binary matrix
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

def countSquares(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i != 0 and j != 0 and matrix[i][j] == 1:
                # Max length of square matrix from this index
                # (in part of matrix we have traversed, i.e., upward left part considering the current index as the center of the graph paper)
                # Max length of square matrix = max squares associated with the current index
                # (in upward left part considering this is the center of the graph paper)
                matrix[i][j] = 1 + min(matrix[i-1][j], min(matrix[i][j-1], matrix[i-1][j-1]))

            count += matrix[i][j]  # Add all squares associated with each index
            # For the max area square submatrix with all ones: ans = max(matrix[i][j], ans)

    return count
