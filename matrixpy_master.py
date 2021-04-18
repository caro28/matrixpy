from matrix_sparse_helper import convert_tuple

class Matrix:
    def __init__(self, elements = [], num_rows = 0, num_cols = 0):
        self.elements = elements
        self.num_rows = num_rows
        self.num_cols = num_cols
    
    def set_elements(self, lst_elements):
        # lst_elements contains elements from row[0][0] to col[n][n]
        self.elements = lst_elements
    
    def set_numrows(self, num_rows):
        self.num_rows = num_rows
    
    def set_numcols(self, num_cols):
        self.num_cols = num_cols
    
    # TODO-question: Are these getter methods below necessary? Given that this data is already stored as attributes?
    def get_numrows(self):
        return self.num_rows
    
    def get_numcols(self):
        return self.num_cols
    
    def get_index(self, row, col):
        '''
        Parameters: row, col of element want to access
        Returns: element at row, col
        '''
        pass
    
    def transpose(self):
        '''
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
        new_matrix.set_numcols(self.set_numrows)

        return new_matrix

    def add_matrix_TEST(self, other):
        '''
        Alternate to add_matrix() using get_index() --> hoping it's simpler!
        '''
        pass
    
    def add_matrix(self, other):
        '''
        Parameters:
            self
            other: other Matrix instance
        Returns:
            matrix_add: a new Matrix instance
        '''
        # check that dimensions of self and other are equal
        if (self.num_rows != other.num_rows and self.num_cols != other.num_cols):
            print("Matrices must be same dimension.")
        else:
            # SCENARIO 1: sparse + rows
            if isinstance(self, MatrixSparse) and isinstance(other, MatrixRows) or isinstance(other, MatrixSparse) and isinstance(self, MatrixRows):
                # create new MatrixRows instance
                matrix_add = MatrixRows(elements=[], num_rows=0, num_cols=0)
                # copy elements of MatrixRows instance to matrix_add
                if isinstance(self, MatrixRows):
                    matrix_add.elements = self.elements[:]
                else:
                    matrix_add.elements = other.elements[:]

                for key in self.elements.keys():
                    # sum non-zero values of self with corresponding values of matrix_add
                    sum_elements = self.elements[key] + matrix_add.elements[key[0]][key[1]]
                    # replace values in matrix_add with new sum
                    matrix_add.elements[key[0]][key[1]] = sum_elements
            
            # SCENARIO 2: sparse + cols --> TODO-move to helper function? copied code from SCENARIO 1
            elif isinstance(self, MatrixSparse) and isinstance(other, MatrixCols) or isinstance(other, MatrixSparse) and isinstance(self, MatrixCols):
                # create new MatrixCols instance
                matrix_add = MatrixCols(elements=[], num_rows=0, num_cols=0)
                other_transposed = other.transpose()
                # copy elements of MatrixCols instance to matrix_add
                if isinstance(self, MatrixCols):
                    matrix_add.elements = self.elements[:]
                else:
                    matrix_add.elements = other_transposed.elements[:]

                for key in self.elements.keys():
                    # sum non-zero values of self with corresponding values of matrix_add
                    sum_elements = self.elements[key] + matrix_add.elements[key[0]][key[1]]
                    # replace values in matrix_add with new sum
                    matrix_add.elements[key[0]][key[1]] = sum_elements

            # SCENARIO 3: rows + rows OR cols + cols
            elif isinstance(self, MatrixRows) and isinstance(other, MatrixRows) or isinstance(self, MatrixCols) and isinstance(other, MatrixCols):
                # create new Matrix instance matching type of self
                if isinstance(self, MatrixRows):
                    matrix_add = MatrixRows(elements=[], num_rows=0, num_cols=0)
                else:
                    matrix_add = MatrixCols(elements=[], num_rows=0, num_cols=0)
                
                # copy elements of self to matrix_add
                matrix_add.elements = self.elements[:]
                i = 0
                j = 0
                
                # replace elements of matrix_add with sums of matching elements from self and other
                while i < len(self.elements):
                    while j < len(self.elements[i]):
                        sum_elements = self.elements[i][j] + other.elements[i][j]
                        matrix_add.elements[i][j] = sum_elements
                        j += 1
                    i += 1
                    j = 0

            # SCENARIO 4: sparse + sparse
            else:
                # create new MatrixSparse object
                matrix_add = MatrixSparse(elements=[], num_rows=0, num_cols=0)
                matrix_add_keys = []
                matrix_add_values = []

                for key_self in self.elements.keys():
                    for key_other in other.elements.keys():
                        # if keys are equal, sum their values and append to matrix_add
                        if key_self == key_other:
                            matrix_add_keys.append(key_self)
                            sum_values = self.elements[key_self] + other.elements[key_other]
                            matrix_add_values.append(sum_values)
                        # append to matrix_add key, value pair from self and other
                        else:
                            matrix_add_keys.append(key_self)
                            matrix_add_values.append(self.elements[key_self])
                            matrix_add_keys.append(key_other)
                            matrix_add_values.append(other.elements[key_other])

                # update elements of matrix_add using matrix_add key and value lists
                for i in range(len(matrix_add_keys)):
                    matrix_add.elements[matrix_add_keys[i]] = matrix_add_values[i]               
                
                # sort by keys
                matrix_add.elements = dict(sorted(matrix_add.elements.items()))            

            # set attributes of matrix_add
            matrix_add.set_numrows = self.num_rows
            matrix_add.set_numcols = self.set_numcols

            return matrix_add


class MatrixSparse(Matrix):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_dict()
    
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

    # TODO-question: need this? Given that this data is already stored as attribute?
    def get_elements_rows(self):
        return self.elements


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
    
    # TODO-question: need this? Given that this data is already stored as attribute?
    def get_elements_cols(self):
        return self.elements



mat_sparse = MatrixSparse(elements=[0, 0, 0, 3, 0, 0, 5, 0, 3], num_rows=3, num_cols=3)
mat_sparse_2 = MatrixSparse(elements = [0, 3, 0, 0, 2, 0, 0, 0, 2], num_rows=3, num_cols=3)
mat_rows = MatrixRows(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_rows_copy = MatrixRows(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_cols = MatrixCols(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)
mat_cols_copy = MatrixCols(elements=[1, 2, 3, 4, 5, 6, 7, 8, 9], num_rows=3, num_cols=3)

#print(mat_sparse.elements)
#print(mat_sparse_2.elements)
new_mat = mat_sparse.add_matrix(mat_sparse_2)
print(new_mat.elements)

#mat_sparse.elements = {(1, 0): 3, (2, 0): 5, (2, 2): 3}
#mat_rows.elements = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#mat_cols.elements = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]