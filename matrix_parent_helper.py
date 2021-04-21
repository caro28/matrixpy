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


OR:

for element in self, element in other:
    self.get_element(0,0) + other.get_element(0,0) --> 5 + 0
    self(0,1) + other(0,1)
    ...
    self(n, n) + other(n,n)


# TODO: delete def test() if don't need anymore
def test(x, row, col):

    for key in x.keys():
        print((row, col) == key)
        if (row, col) == key:
            element = x[key]
        else:
            # if (row, col) does not match a key, then element is 0
            element = 0

    return element

x = {(0, 1): 3, (1, 1): 2, (2, 2): 2}
print(test(x, 1, 1))
'''


def nstd_to_simple(x, num_rows, num_cols):
    simple_lst = []
    i = 0
    j = 0

    while i < num_rows:
        while j < num_cols:
            simple_lst.append(x[i][j])
            j += 1
        i += 1
        j = 0
    
    return simple_lst
