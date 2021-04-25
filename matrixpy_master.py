from matrix_sparse_helper import convert_tuple
from matrix_parent_helper import nstd_to_simple

class Matrix:
    '''
    Parent class for Matrix instance.
    Attributes: elements (list), num_rows (int), num_cols (int)
    Methods: getter/setter, matrix operations, change matrix shape of parent 
    class instance
    '''
    def __init__(self, elements = [], num_rows = 0, num_cols = 0):
        self.elements = elements
        self.num_rows = num_rows
        self.num_cols = num_cols

    def set_elements(self, lst_elements):
        '''
        Sets attribute, self.elements
        Parameters:
            lst_elements: (list) list of matrix elements
        Returns:
            None
        '''
        # lst_elements contains elements from row[0][0] to col[n][n]
        self.elements = lst_elements
    
    def get_elements(self):
        '''
        Retrieves attribute, self.elements
        Parameters:
            None
        Returns:
            self.elements: (list) list of matrix elements as attribute
        '''
        return self.elements
    
    def set_numrows(self, num_rows):
        '''
        Sets attribute, self.num_rows
        Parameters:
            num_rows: (int) number of rows in matrix instance
        Returns:
            None
        '''
        self.num_rows = num_rows
    
    def set_numcols(self, num_cols):
        '''
        Sets attribute, self.num_cols
        Parameters:
            num_cols: (int) number of columns in matrix instance
        Returns:
            None
        '''
        self.num_cols = num_cols
    
    def get_numrows(self):
        '''
        Retrieves attribute, self.num_rows
        Parameters:
            None
        Returns:
            self.num_rows: (list) number of matrix rows as attribute
        '''
        return self.num_rows
    
    def get_numcols(self):
        '''
        Retrieves attribute, self.num_cols
        Parameters:
            None
        Returns:
            self.num_cols: (list) number of matrix columns as attribute
        '''
        return self.num_cols
    
    def change_matrix_shape(self, matrix_type):
        '''
        Changes shape of parent class matrix to any subclass shape
        Parameters:
            matrix_type: (str) shape of output (MatrixRows, 
            MatrixCols, MatrixSparse)
        Returns:
            new matrix instance of requested subclass shape
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")
        
        return matrix_type(elements=self.elements, num_rows=self.num_rows, num_cols=self.num_cols)

    def get_value(self, row, col):
        '''
        Access a matrix element.
        Parameters: 
            row: (int) row number of element to access
            col: (int) col number of element to access
        Returns: 
            element: (int or float) matrix element
        '''
        # check matrix instance type
        if isinstance(self, MatrixRows) or isinstance(self, MatrixCols):
            if isinstance(self, MatrixRows):
                return self.elements[row][col]
            else:
                return self.elements[col][row]

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

        # matrix instance is parent class
        else:
            # indexing formula from Professor Bemis's lecture 10 slides
            return self.elements[row * self.num_rows + col]

        return element

    def transpose(self):
        '''
        Transposes a matrix instance. Should be called on MatrixRows or 
        MatrixCols instance only.
        Parameters:
            None
        Returns:
            new_matrix: new matrix instance
        '''
        # print error message if self is not MatrixRows or MatrixCols instance
        if not isinstance(self, MatrixRows) and not isinstance(self, MatrixCols):
            print("The transpose method should only be used with MatrixRows or MatrixCols instance")
        
        else:
            # create new Matrix object
            new_matrix = Matrix(elements=[], num_rows=0, num_cols=0)

            # initialize empty nested list
            nested_lst = [[] for i in range(len(self.elements))]

            i = 0
            j = 0

            while i < len(self.elements):
                while j < (len(self.elements[i])):
                    nested_lst[i].append(self.elements[j][i])
                    j += 1
                i += 1
                j = 0

            # set attributes of new_matrix
            new_matrix.elements = nested_lst
            new_matrix.set_numrows(self.num_cols)
            new_matrix.set_numcols(self.num_rows)

            return new_matrix

    def add_matrix(self, other):
        '''
        Adds one matrix instance with another matrix instance. Calls method
        Matrix.get_value().
        Parameters: 
            other: Matrix instance
        Returns:
            matrix_add: (Matrix instance) Defaults to MatrixRows shape
        '''
        # print error message if dimensions of self and other are not equal
        if (self.num_rows != other.num_rows and self.num_cols != other.num_cols):
            print("Matrices must be same dimension.")
        
        else:
            matrix_add = Matrix(elements=[], num_rows=self.num_rows,\
                num_cols=self.num_cols)

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
        Subtract one matrix instance from another matrix instance. Calls
        methods Matrix.scalar_multiply() and Matrix.add_matrix().
        Parameters: 
            other: (Matrix instance)
        Returns:
            sub_matrix: (Matrix instance) Defaults to MatrixRows shape
        '''
        other = other.scalar_multiply(-1)
        sub_matrix = self.add_matrix(other)

        return sub_matrix
    
    def scalar_multiply(self, num):
        '''
        Multiplies a matrix instance with a scalar
        Parameters:
            num: (int or float) number to multiply against self
        Returns:
            mat_scaled: (Matrix object) new matrix object with same shape as 
            self
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
        
        # dict
        elif isinstance(self, MatrixSparse):
            mat_scaled.elements = self.elements.copy()

            for key in mat_scaled.elements.keys():
                mat_scaled.elements[key] *= num
        
        # simple list
        else:
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
        Divide a matrix instance by a scalar. Calls method 
        Matrix.scalar_multiply()
        Parameters:
            num: (int or float) number to divide against self
        Returns:
            mat_scaled: (Matrix object) new matrix object with same shape as self
        '''
        new_num = 1/num
        return self.scalar_multiply(new_num)

    def slice_matrix(self, row_start, row_finish, col_start, col_finish):
        '''
        Slices a matrix, returning the slice as a list of elements. Calls
        method Matrix.get_value().
        Parameters:
            row_start:(int) index of row where slice begins
            row_finish: (int) index of row where slice ends
            col_start: (int) index of column where slice begins
            col_finish: (int) index of column where slice ends
        Returns:
            sliced_elements: (list, nested list, or dict) inclusive of 
            row_finish and col_finish. 
            sliced_elements is a list if the slice draws from one row or one
            column only.
            sliced_elements is a nested list if the slice crosses both rows and
            columns. sliced_elements defaults to being organized by rows. 
            sliced_elements is a dict if the method is called on a 
            MatrixSparse instance. Non-zero elements only are included.
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

    def dot_product(self, row, col, r_row_start, r_col_start, r_num_cols,\
        c_row_start, c_col_start, c_num_rows):
        '''
        Calculates and returns the dot product of a matrix row and matrix column
        Parameters:
            row: (list)
            col: (list)
            r_row_start:(int) for row input, index of row where slice begins
            r_col_start: (int) for row input, index of column where slice begins
            r_num_cols: (int) for row input, number of columns of original matrix
            c_row_start: (int) for col input, index of row where slice begins
            c_col_start: (int) for col input, index of column where slice begins
            c_num_rows: (int) for col input, number of rows of original matrix
        Returns:
            dot_product (int or float)
        '''
        dot_product = 0

        # check data type of row and column inputs
        if isinstance(row, dict):
            keys_list = list(row)
            row_list = []
            i = 0
            j = 0

            # convert row to a list, adding 0 for elements not in dict
            while i < r_num_cols:
                while j < len(keys_list):
                    if keys_list[j] == tuple([r_row_start, r_col_start]):
                        row_list.append(row[keys_list[j]])
                        r_col_start += 1
                        i += 1
                        j += 1
                    else:
                        row_list.append(0)
                        r_col_start += 1
                        i += 1
                
                # end iteration if have reached end of row
                if i == r_num_cols:
                    i += 1
                else:
                    row_list.append(0)
                    i += 1
                
            row = row_list
        
        # repeat logic above for column input
        if isinstance(col, dict):
            keys_list = list(col)
            col_list = []
            i = 0
            j = 0

            # convert column to a list, adding 0 for elements not in dict
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

                # end iteration if reached end of column                
                if i == c_num_rows:
                    i += 1
                else:
                    col_list.append(0)
                    i += 1
            
            col = col_list

        # print error messahe if dimensions of row and col are not equal
        if len(row) != len(col):
            print("Inputs must be same dimension.")
        
        else:
            i = 0
            while i < len(row):
                dot_product += row[i] * col[i]
                i += 1
        
        return dot_product

    def multiply_matrix(self, other):
        '''
        Multiplies a matrix instance against another matrix instance. Calls
        methods Matrix.slice_matrix() and Matrix.dot_product().
        Parameters: 
            other: (Matrix instance)
        Returns:
            mult_matrix: (Matrix instance) defaults to MatrixRows shape
        '''
        # check that dimensions are compatible for multiplication
        if self.num_cols != other.num_rows:
            print("Number of columns of matrix A must equal number of rows of"\
                "matrix B in A * B.")
        
        else:
            # create new Matrix instance
            new_matrix = Matrix(elements=[], num_rows=self.num_rows,\
                num_cols=other.num_cols)
            i = 0
            j = 0

            while i < self.num_rows:
                while j < other.num_cols:
                    # slice row and column in pairs
                    row = self.slice_matrix(i, i, 0, self.num_cols - 1)
                    col = other.slice_matrix(0, other.num_rows - 1, j, j)
                    # calculate dot product of each pair
                    element = self.dot_product(row, col, i, 0, self.num_cols,\
                        0, j, other.num_rows)
                    # append to new_matrix self.elements
                    new_matrix.elements.append(element)
                    j += 1
                i += 1
                j = 0
            
            # change shape to MatrixRows
            mult_matrix = new_matrix.change_matrix_shape(MatrixRows)

            return mult_matrix


class MatrixSparse(Matrix):
    '''
    Subclass of Matrix instance
    Attributes: elements (list), num_rows (int), num_cols (int), from parent
    class
    Methods: 
        From parent class: getter/setter, matrix operations
        From MatrixSparse subclass: methods to set self.elements as a dict,
        change matrix shape (MatrixSparse only implementation)
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_dict()
    
    def create_dict(self):
        '''
        Creates a dict for non-zero elements of matrix. Keys are tuple listing
        their position in the matrix (row, col). Values are the elements. Calls
        convert_tuple() from matrix_sparse_helper.py to generate tuples for 
        keys.
        Parameters:
            None
        Returns:
            matrix_dict: (dict) non-zero elements of matrix instance
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
    
    def set_dict(self):
        '''
        Sets dict returned by MatrixSparse.create_dict() as self.elements
        Parameters:
            None
        Returns:
            None
        '''
        self.elements = self.create_dict()

    def get_dct_lst(self):
        '''
        Converts elements from dict to list, adding 0 for elements not in dict.
        Used by MatrixSparse.change_matrix_shape() only when changing shape of
        MatrixSparse to a subclass with list as underlying data structure.
        Parameters:
            None
        Returns:
            lst_elements: (list) list of zero and non-zero elements
        '''
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
        Changes shape of MatrixSparse instance to another subclass. Cannot
        change shape to parent class.
        Parameters:
            matrix_type: (str) shape of output (MatrixRows, 
            MatrixCols)
        Returns:
            new matrix instance of requested subclass shape
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")
        
        # convert dict to simple list
        else:
            simple_lst = self.get_dct_lst()

            return matrix_type(elements=simple_lst, num_rows=self.num_rows, num_cols=self.num_cols)


class MatrixRows(Matrix):
    '''
    Subclass of Matrix instance
    Attributes: elements (list), num_rows (int), num_cols (int), from parent
    class
    Methods: 
        From parent class: getter/setter, matrix operations
        From MatrixRows subclass: methods to set self.elements as a nested 
        list, change matrix shape (MatrixRows only implementation)
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # run method set_rows() to organize by rows
        self.set_rows()
    
    def set_rows(self):
        '''
        Changes shape of self.elements to a nested list
        Parameters:
            None
        Returns:
            None
        '''
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
        '''
        Converts elements from nested list to list. Used by 
        MatrixRows.change_matrix_shape() only when changing shape of MatrixRows
        instance to a different subclass.
        Parameters:
            None
        Returns:
            list of elements
        '''
        return nstd_to_simple(self.elements, self.num_rows, self.num_cols)
    
    def change_matrix_shape(self, matrix_type):
        '''
        Changes shape of MatrixRows instance to another subclass. Cannot
        change shape to parent class.
        Parameters:
            matrix_type: (str) shape of output (MatrixCols, 
            MatrixSparse)
        Returns:
            new matrix instance of requested subclass shape
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")
        
        # convert input data type to simple list
        else:
            simple_lst = self.get_simple_lst()
            
            return matrix_type(elements=simple_lst, num_rows=self.num_rows, num_cols=self.num_cols)


class MatrixCols(Matrix):
    '''
    Subclass of Matrix instance
    Attributes: elements (list), num_rows (int), num_cols (int), from parent
    class
    Methods: 
        From parent class: getter/setter, matrix operations
        From MatrixCols subclass: methods to set self.elements as a nested 
        list, change matrix shape (MatrixCols only implementation)
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # run method convert_col() to organize by columns
        self.set_cols()

    def set_cols(self):
        '''
        Changes shape of self.elements to a nested list
        Parameters:
            None
        Returns:
            None
        '''
        # initialize empty nested list
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
        '''
        Converts elements from nested list to list. Used by 
        MatrixCols.change_matrix_shape() only when changing shape of MatrixCols
        instance to a different subclass. Calls MatrixCols.transpose().
        Parameters:
            None
        Returns:
            list of elements
        '''
        new_mat = self.transpose()

        return nstd_to_simple(new_mat.elements, new_mat.num_rows, new_mat.num_cols)
    
    def change_matrix_shape(self, matrix_type):
        '''
        Changes shape of MatrixCols instance to another subclass. Cannot
        change shape to parent class.
        Parameters:
            matrix_type: (str) shape of output (MatrixRows, 
            MatrixSparse)
        Returns:
            new matrix instance of requested subclass shape
        '''
        # print error message if matrix_type == type(self)
        if isinstance(self, matrix_type):
            print("matrix_type must be a different Matrix subclass")

        # convert input data type to simple list
        else:
            simple_lst = self.get_simple_lst()

            return matrix_type(elements=simple_lst, num_rows=self.num_rows, num_cols=self.num_cols)