from math import floor

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

class MatrixSparse(Matrix):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_dict()
    
    def create_dict(self):
        '''
        Returns a dict whose values are the non-zero elements of lst_elements
        and keys are a tuple listing their position in the matrix (row, col).
        TODO: move code building the tuples into a separate method (or 
        separate file, as a helper function), once this works.
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

        # get row numbers from elem_indices
        row_num = []
        for index in elem_indices:
            if index < self.num_cols:
                row_num.append(0)
            elif index == self.num_cols:
                row_num.append(1)
            else:
                row = floor(index / self.num_cols) - 1
                row_num.append(row)
        
        # get col numbers from elem_indices
        col_num = []
        for index in elem_indices:
            if index < self.num_cols:
                col_num.append(index)
            else:
                col = index % self.num_cols
                col_num.append(col)

        # TODO: combine row numbers, col numbers into tuples

        # TODO: changes keys so that they are the tuples just created
        matrix_dict = {}
        for j in range(len(elem_indices)):
            matrix_dict[elem_indices[j]] = non_zero_elem[j]

        return matrix_dict
    
        
                

    # TODO-question: ok to rename this set_elements()? Would this just override the method in Matrix parent class?
    def set_dict(self):
        self.elements = self.create_dict()



y = MatrixSparse(elements=[0, 0, 0, 3, 0, 0, 5, 0, 3], num_rows=3, num_cols=3)
print(y.elements)


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
            #print(i)
        
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



