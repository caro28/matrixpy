from matrix_sparse_helper import convert_tuple
from matrix_parent_helper import nstd_to_simple

class Matrix:
    def __init__(self, elements = [], num_rows = 0, num_cols = 0):
        self.elements = elements
        self.num_rows = num_rows
        self.num_cols = num_cols

    def set_elements(self, lst_elements):
        # lst_elements contains elements from row[0][0] to col[n][n]
        self.elements = lst_elements
    
    def get_elements(self):
        return self.elements
    
    def set_numrows(self, num_rows):
        self.num_rows = num_rows
    
    def set_numcols(self, num_cols):
        self.num_cols = num_cols
    
    def get_numrows(self):
        return self.num_rows
    
    def get_numcols(self):
        return self.num_cols
    
    def change_matrix_shape(self, matrix_type):
        '''
        Parameters:
            matrix_type: (str) Matrix subclass of output (MatrixRows, MatrixCols, MatrixSparse)
        Returns:
            new matrix object
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")
        
        return matrix_type(elements=self.elements, num_rows=self.num_rows, num_cols=self.num_cols)


    def get_value(self, row, col):
        '''
        Parameters: 
            row, col: (int) row, col of element want to access
        Returns: 
            element: (int or float) element at (row, col)
        '''
        # if elements are in nested list
        if isinstance(self, MatrixRows) or isinstance(self, MatrixCols):
            if isinstance(self, MatrixRows):
                return self.elements[row][col]
            else:
                # TODO: necessary to transpose? instead, return self.elements[col][row]
                # col represents outer list
                #mat_transposed = self.transpose()
                #return mat_transposed.elements[row][col]
                return self.elements[col][row]

        # elements are in dict
        elif isinstance(self, MatrixSparse):
            # access element using keys
            for key in self.elements.keys():
                # check if (row, col) corresponds to an existing key
                if (row, col) == key:
                    # stop iteration if find matching key
                    return self.elements[key]
                else:
                    # keep iterating until reach end of keys; element = 0 if no match
                    element = 0
            
        # elements are in simple list
        else:
            # based on Prof Bemis's lecture 10
            return self.elements[row * self.num_rows + col]

        return element


    def transpose(self):
        '''
        # TODO: mutate object instead? In change shape, when converting MatrixCols to simple list, 
        # means creating new matrix object - original matrix doesn't change shape.
        Returns new matrix object
        '''
        # create new Matrix object
        new_matrix = Matrix(elements=[], num_rows=0, num_cols=0)
        
        nested_lst = [[] for i in range(len(self.elements))]

        i = 0
        j = 0

        while i < len(self.elements):
            while j < (len(self.elements[i])):
                nested_lst[i].append(self.elements[j][i])
                j += 1
            i += 1
            j = 0

        new_matrix.elements = nested_lst
        new_matrix.set_numrows(self.num_cols)
        new_matrix.set_numcols(self.num_rows)

        return new_matrix

    def add_matrix(self, other):
        '''
        Parameters: 
            self, other: (Matrix instances)
        Returns:
            matrix_add: (Matrix instance) Defaults to MatrixRows shape
        '''
        # check that dimensions of self and other are equal
        if (self.num_rows != other.num_rows and self.num_cols != other.num_cols):
            print("Matrices must be same dimension.")
        else:
            matrix_add = Matrix(elements=[], num_rows=self.num_rows, num_cols=self.num_cols)

            i = 0
            j = 0

            # add matching elements of self and other
            while i < self.num_rows:
                while j < self.num_cols:
                    sum_elements = self.get_value(i, j) + other.get_value(i, j)
                    matrix_add.elements.append(sum_elements)
                    j += 1
                i += 1
                j = 0
            
            # change to default shape
            matrix_add = matrix_add.change_matrix_shape(MatrixRows)

            return matrix_add

    def subtract_matrix(self, other):
        '''
        Parameters: 
            self, other: (Matrix instances)
        Returns:
            sub_matrix: (Matrix instance) Defaults to MatrixRows shape
        '''
        other = other.scalar_multiply(-1)
        sub_matrix = self.add_matrix(other)

        return sub_matrix
    
    def scalar_multiply(self, num):
        '''
        Parameters:
            num: (int or float) number to multiply against self
        Returns:
            mat_scaled: (Matrix object) new matrix object with same shape as self
        '''
        # create a new matrix object
        matrix_type = type(self)
        mat_scaled = matrix_type(elements=[], num_rows=0, num_cols=0)
        
        # check type of self - nested list
        if isinstance(self, MatrixRows) or isinstance(self, MatrixCols):
            # create copy of self.elements
            mat_scaled.elements = self.elements[:]

            i = 0
            j = 0

            while i < len(mat_scaled.elements):
                while j < len(mat_scaled.elements[i]):
                    mat_scaled.elements[i][j] *= num
                    j += 1
                i += 1
                j = 0
        
        elif isinstance(self, MatrixSparse): # dict
            mat_scaled.elements = self.elements.copy()

            for key in mat_scaled.elements.keys():
                mat_scaled.elements[key] *= num
        
        else: # simple list
            # create copy of self.elements
            mat_scaled.elements = self.elements[:]
            for i in range(len(mat_scaled.elements)):
                mat_scaled.elements[i] *= num
        
        # set attributes of mat_scaled
        mat_scaled.set_numrows(self.num_rows)
        mat_scaled.set_numcols(self.num_cols)

        return mat_scaled

    def scalar_divide(self, num):
        '''
        Parameters:
            num: (int or float) number to divide against self
        Returns:
            mat_scaled: (Matrix object) new matrix object with same shape as self
        '''
        new_num = 1/num
        return self.scalar_multiply(new_num)

    def slice_matrix(self, row_start, row_finish, col_start, col_finish):
        '''
        Parameters:
            row_start, row_finish, col_start, col_finish: (int) row or col index
        Returns:
            sliced_elements: (list or nested list) inclusive of row_finish and col_finish
                if sliced_elements is nested, default is organized by rows
        '''
        # check Matrix instance type
        if isinstance(self, MatrixSparse):
            sliced_elements = {}
            sliced_keys = []
            sliced_values = []
            for key in self.elements.keys():
                # key/value pairs to include in slice
                if key[0] >= row_start and key[0] <= row_finish and key[1] >= col_start and key[1] <= col_finish:
                    sliced_keys.append(key)
                    sliced_values.append(self.elements[key])
            
            # populate dict
            for i in range(len(sliced_keys)):
                sliced_elements[sliced_keys[i]] = sliced_values[i]
            
        else:
            sliced_elements = []

            # if slicing a single row
            if row_start == row_finish:
                while col_start < (col_finish + 1):
                    element = self.get_value(row_start, col_start)
                    sliced_elements.append(element)
                    col_start += 1
        
            # if slicing a single col
            elif col_start == col_finish:
                while row_start < (row_finish + 1):
                    element = self.get_value(row_start, col_start)
                    sliced_elements.append(element)
                    row_start += 1

            # if slicing rows and columns
            else:
                # initialize nested list with len == num_rows in slice
                sliced_elements = [[] for i in range(row_finish + 1)]
                i = 0
                j = 0

                while i < (row_finish + 1):
                    while j < (col_finish + 1):
                        element = self.get_value(row_start, col_start)
                        sliced_elements[i].append(element)
                        j += 1
                        col_start += 1
                    i += 1
                    j = 0
                    row_start += 1
                    col_start = 0
    
        return sliced_elements


    def dot_product(self, row, col, r_row_start, r_col_start, r_num_cols, c_row_start, c_col_start, c_num_rows):
        '''
        Parameters:
            row, col: (lists)
        Returns:
            dot_product (int or float)
        '''
        # TODO: This is just a test ----------> delete after figuring out bug
        #if type(row).__name__ == 'dict':
            #print("row is a dict: do something")

        #if type(col).__name__ == 'dict':
            #print("col is a dict: do something")
        
        dot_product = 0

        if isinstance(row, dict):
            keys_list = list(row)
            row_list = []
            i = 0
            j = 0
            #print(keys_list)

            while i < r_num_cols:
                while j < len(keys_list):
                    #print(keys_list[j])
                    #print(j)
                #for key in row.keys():
                    #print(keys_list[j] == tuple([r_row_start, r_col_start]))
                    if keys_list[j] == tuple([r_row_start, r_col_start]):
                    #if key == tuple([r_row_start, r_col_start]):
                        row_list.append(row[keys_list[j]])
                        #row_list.append(row[key])
                        r_col_start += 1
                        i += 1
                        j += 1
                    else:
                        row_list.append(0)
                        r_col_start += 1
                        i += 1
                        #j += 1
                
                #TODO - check ok to delete any of these below
                if i == r_num_cols:
                    i += 1
                else:
                    row_list.append(0)
                    i += 1
                
            row = row_list
            #print(row)
        
        if isinstance(col, dict):
            keys_list = list(col)
            col_list = []
            i = 0
            j = 0
            while i < c_num_rows:
                while j < len(keys_list):
                    if keys_list[j] == tuple([c_row_start, c_col_start]):
                        col_list.append(col[keys_list[j]])
                        c_row_start += 1
                        i += 1
                        j += 1
                    else:
                        col_list.append(0)
                        c_row_start += 1
                        i += 1
                        #j += 1
                
                if i == c_num_rows:
                    i += 1
                else:
                    col_list.append(0)
                    i += 1
            
            col = col_list

        # check that dimensions of row and col are equal
        if len(row) != len(col):
            print("Inputs must be same dimension.")
        else:
            i = 0
            #TODO-delete: dot_product = 0
            while i < len(row):
                dot_product += row[i] * col[i]
                #print(row[i])
                #print(col[i])
                i += 1
        
        return dot_product


    def multiply_matrix(self, other):
        '''
        Parameters: 
            self, other: (Matrix instances)
        Returns:
            mult_matrix: (Matrix instance) defaults to MatrixRows shape
        '''
        # check that dimensions are compatible for multiplication
        if self.num_cols != other.num_rows:
            ("Number of columns of matrix A must equal number of rows of matrix B in A * B.")
        
        else:
            # create new Matrix instance
            new_matrix = Matrix(elements=[], num_rows=self.num_rows, num_cols=other.num_cols)
            i = 0
            j = 0

            while i < self.num_rows:
                while j < other.num_cols:
                    row = self.slice_matrix(i, i, 0, self.num_cols - 1)
                    col = other.slice_matrix(0, other.num_rows - 1, j, j)
                    element = self.dot_product(row, col, i, 0, self.num_cols, 0, j, other.num_rows)
                    new_matrix.elements.append(element)
                    j += 1
                i += 1
                j = 0
            
            mult_matrix = new_matrix.change_matrix_shape(MatrixRows)

            return mult_matrix


class MatrixSparse(Matrix):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_dict()
    
    # TODO-question: need to sort dict by keys here so that iterating through keys elsewhere will preserve keys' order?
    def create_dict(self):
        '''
        Returns a dict whose values are the non-zero elements of lst_elements
        and keys are a tuple listing their position in the matrix (row, col).
        Use helper function to generate position tuples from 
        matrix_sparse_helper.py
        '''
        non_zero_elem = []
        elem_indices = []

        # retrieve non-zero elements and their index
        i = 0
        while i < len(self.elements):
            if self.elements[i] != 0:
                non_zero_elem.append(self.elements[i])
                elem_indices.append(i)
                i += 1
            else:
                i += 1
        
        # convert index to tuples listing position in matrix (row, col)
        matrix_pos_lst = convert_tuple(elem_indices, self.num_cols)

        # create dict of non-zero matrix elements
        matrix_dict = {}
        for i in range(len(matrix_pos_lst)):
            matrix_dict[matrix_pos_lst[i]] = non_zero_elem[i]

        return matrix_dict
    
    # TODO-question: ok to rename this set_elements()? Would this just override the method in Matrix parent class?
    def set_dict(self):
        self.elements = self.create_dict()

    def get_dct_lst(self):
        lst_elements = []
    
        i = 0
        j = 0

        while i < self.num_rows:
            while j < self.num_cols:
                element = self.get_value(i, j)
                lst_elements.append(element)
                j += 1
            i += 1
            j = 0
        
        return lst_elements
  
    def change_matrix_shape(self, matrix_type):
        '''
        Parameters:
            matrix_type: (str) Matrix subclass of output (MatrixRows, MatrixCols, MatrixSparse)
        Returns:
            new matrix object
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")
        
        # convert dict to simple list
        else:
            simple_lst = self.get_dct_lst()

            return matrix_type(elements=simple_lst, num_rows=self.num_rows, num_cols=self.num_cols)


class MatrixRows(Matrix):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # run method set_rows() to organize by rows
        self.set_rows()
    
    def set_rows(self):
        # created nested list with len = num_rows
        nested_lst_rows = [[] for i in range(self.num_rows)]

        i = 0
        j = 0

        while j < len(self.elements):
            while len(nested_lst_rows[i]) < self.num_cols:
                nested_lst_rows[i].append(self.elements[j])
                j += 1
            i += 1
        
        self.elements = nested_lst_rows
    
    def get_simple_lst(self):
        return nstd_to_simple(self.elements, self.num_rows, self.num_cols)
    
    def change_matrix_shape(self, matrix_type):
        '''
        Parameters:
            matrix_type: (str) Matrix subclass of output (MatrixRows, MatrixCols, MatrixSparse)
        Returns:
            new matrix object
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")
        
        # convert input data type to simple list
        else:
            simple_lst = self.get_simple_lst()
            
            return matrix_type(elements=simple_lst, num_rows=self.num_rows, num_cols=self.num_cols)


class MatrixCols(Matrix):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # run method convert_col() to organize by columns
        self.set_cols()

    def set_cols(self):
        # initialize empty nested list that can be updated individually
        # (Prof Bemis showed us how to do this in lecture one day)
        nested_lst_cols = [[] for i in range(self.num_cols)]

        i = 0
        j = 0

        while j < len(self.elements):
            while len(nested_lst_cols[i]) < self.num_rows:
                nested_lst_cols[i].append(self.elements[j])
                j += self.num_cols
            i += 1

            if i < len(nested_lst_cols):
                # begin inner while loop at next index of self.elements
                j = i
            else:
                # end the while loop
                j = len(self.elements)

        self.elements = nested_lst_cols
    

    def get_simple_lst(self):
        new_mat = self.transpose()

        return nstd_to_simple(new_mat.elements, new_mat.num_rows, new_mat.num_cols)
    

    def change_matrix_shape(self, matrix_type):
        '''
        Parameters:
            matrix_type: (str) Matrix subclass of output (MatrixRows, MatrixCols, MatrixSparse)
        Returns:
            new matrix object
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")

        # convert input data type to simple list
        else:
            simple_lst = self.get_simple_lst()

            return matrix_type(elements=simple_lst, num_rows=self.num_rows, num_cols=self.num_cols)
    


# TESTS
mat_sparse = MatrixSparse(elements=[0, 0, 0, 3, 0, 0, 5, 0, 3], num_rows=3, num_cols=3)
mat_sparse_2 = MatrixSparse(elements = [0, 3, 0, 0, 1, 0, 0, 0, 2], num_rows=3, num_cols=3)
mat_rows = MatrixRows(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_rows_copy = MatrixRows(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_cols = MatrixCols(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_cols_copy = MatrixCols(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_simple = Matrix(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_simple2 = Matrix(elements=[2, 4, 6, 8, 10, 12, 14, 16, 18], num_rows=3, num_cols=3)

#mat_sparse.elements = {(1, 0): 4, (2, 0): 5, (2, 2): 6}
#mat_sparse_2.elements = {(0, 1): 3, (1, 1): 2, (2, 2): 2}
#mat_rows.elements = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#mat_cols.elements = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# test add_matrix()
#new_mat = mat_sparse.add_matrix(mat_simple)
#print(new_mat.elements)

# test scalar_multiply()
#new_mat = mat_rows.scalar_multiply(0)
#print(new_mat.elements)

# test subtract_matrix()
#sub1 = mat_rows.subtract_matrix(mat_simple)
#sub2 = mat_sparse.subtract_matrix(mat_cols)
#sub3 = mat_simple.subtract_matrix(mat_sparse)

#print(sub1.elements)
#print(sub2.elements)
#print(sub3.elements)


# test scalar_divide()
# new_mat = mat_sparse.scalar_divide(-2)
# print(new_mat.elements)


# test dot_product()
#slice1 = mat_simple.slice_matrix(0, 2, 2, 2)
#slice2 = mat_sparse.slice_matrix(2, 2, 0, 2)
#slice3 = mat_rows.slice_matrix(0, 2, 1, 1)
#slice4 = mat_sparse_2.slice_matrix(0, 2, 1, 1)
#print(slice2)
#print(mat_sparse.dot_product(slice2, slice3, 2, 0, 3, 0, 1, 3))



# test slice_matrix()
#print(mat_simple.slice_matrix(0, 2, 1, 2))
#print(mat_sparse.slice_matrix(1, 2, 1, 2))
#print(mat_rows.slice_matrix(2, 2, 0, 2))
#print(mat_cols.slice_matrix(0, 0, 1, 2))

# test change_matrix_shape()
#test1 = mat_simple.change_matrix_shape(MatrixRows)
# test2 = mat_simple.change_matrix_shape(MatrixSparse)
test3 = mat_cols.change_matrix_shape(MatrixRows)
print(test3.elements)

# test get_element_lst()
#print(mat_sparse.get_elements_lst())

# test multiply_matrix()
#mult1 = mat_simple.multiply_matrix(mat_rows)
#print(mult1.elements)