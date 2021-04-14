from matrixpy_master import Matrix, MatrixRows, MatrixCols

# TODO: convert to unit tests for methods of Matrix, MatrixRows, MatrixCols
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_rows = MatrixRows(elements=elements, num_rows=3, num_cols=3)
test_cols = MatrixCols(elements=elements, num_rows=3, num_cols=3)

print(test_rows.elements) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(test_cols.elements) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

