'''
A = sparse matrix
B = dense matrix

add_matrix():
if A[0,0] == None:
    new_matrix[0,0] = B[0,0]
elif B[0,0] == None:
    new_matrix[0,0] = A[0,0]
else:
    new_matrix[0,0] = A[0,0] + B[0,0]

multiply_matrix():
if A[0,0] == None:
    new_matrix[0,0] = B[0,0] * 0
elif B[0,0] == None:
    new_matrix[0,0] = A[0,0] * 0
else:
    new_matrix[0,0] = A[0,0] * B[0,0]

'''
